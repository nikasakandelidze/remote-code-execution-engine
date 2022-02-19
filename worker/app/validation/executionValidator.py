from core.domain import ExecutionInput


class ExecutionValidator:
    def __init__(self):
        pass

    def validate(self, input: ExecutionInput) -> bool:
        return input.code != "" and input.language != ""
