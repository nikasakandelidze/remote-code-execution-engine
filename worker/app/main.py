from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from core.domain import ExecutionInput, ExecutionOutput
from core.codeExecutor import CodeExecutor
from validation.executionValidator import ExecutionValidator

app = FastAPI()
execution_validator = ExecutionValidator()
code_executor = CodeExecutor(execution_validator)


class CodeInput(BaseModel):
    code: Optional[str]
    language: Optional[str]


@app.get("/healthcheck/")
async def health_check():
    return {"status": "OK"}


@app.post("/execute/")
async def execute_code(code_input: CodeInput):
    code = code_input.code
    language = code_input.language
    output: ExecutionOutput = code_executor.execute_code(ExecutionInput(code, language))
    return {"status": output.status, "message": output.output, "hint": output.hint}