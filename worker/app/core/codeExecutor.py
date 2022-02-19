import subprocess

from core.domain import ExecutionInput, ExecutionOutput
from validation.executionValidator import ExecutionValidator
from adapter.fileSystemAdapter import write_content_in_random_file

statuses = {
    "not_valid": 400,
    "error": 500,
    "good": 200
}

messages = {
    "not_valid": "Execution input is note valid, either code or langauge is empty",
    "error":"Sorry, there appears to be a problem."
}

hints = {
    "not_valid": "Check if code and language are both present in input",
    "error": "Check if code and language are both present in input",
    "good": ''
}


class CodeExecutor:
    def __init__(self, validator: ExecutionValidator):
        self.validator = validator

    def execute_code(self, input: ExecutionInput) -> ExecutionOutput:
        if self.validator.validate(input):
            file_name = write_content_in_random_file(input.code, input.language)
            try:
                process = subprocess.Popen(['python', file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()
                if err:
                    return ExecutionOutput(statuses['error'], err.decode("utf-8") , hints['error'])
                else:
                    return ExecutionOutput(statuses['good'], out.decode("utf-8") , hints['good'])
            except Exception:
                return ExecutionOutput(statuses['error'], messages['error'], hints['good'])

        else:
            return ExecutionOutput(statuses['not_valid'], messages['not_valid'], hints["not_valid"])