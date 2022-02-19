
class ExecutionInput:
    def __init__(self, code: str, language: str):
        self.code = code
        self.language = language


class ExecutionOutput:
    def __init__(self, status: int, output: str, hint: str):
        self.status = status
        self.output = output
        self.hint = hint