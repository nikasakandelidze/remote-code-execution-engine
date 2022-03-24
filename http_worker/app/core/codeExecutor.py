import subprocess

from core.domain import ExecutionInput, ExecutionOutput
from validation.executionValidator import ExecutionValidator
from adapter.fileSystemAdapter import write_content_in_random_file
import os

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

cli_runtime_for_language = {
    "python":"python",
    "javascript": "node"
}


class CodeExecutor:
    def __init__(self, validator: ExecutionValidator):
        self.validator = validator

    def get_cli_command_for_language(self, language) -> str:
        return cli_runtime_for_language[language]

    def execute_code(self, input: ExecutionInput) -> ExecutionOutput:
        if self.validator.validate(input):
            file_name = write_content_in_random_file(input.code, input.language)
            try:
                command = self.get_cli_command_for_language(input.language.lower())
                process = subprocess.Popen([command, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()
                if err:
                    return ExecutionOutput(statuses['error'], err.decode("utf-8") , hints['error'])
                else:
                    return ExecutionOutput(statuses['good'], out.decode("utf-8") , hints['good'])
            except Exception as e:
                print(e)
                return ExecutionOutput(statuses['error'], messages['error'], hints['good'])
            finally:
                if file_name:
                    os.remove(file_name)

        else:
            return ExecutionOutput(statuses['not_valid'], messages['not_valid'], hints["not_valid"])