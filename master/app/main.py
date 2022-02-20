from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from core.gatewayService import GatewaySevice

app = FastAPI()


class CodeInput(BaseModel):
    code: Optional[str]
    language: Optional[str]


service = GatewaySevice()

@app.post("/api/run/")
async def execute_code(code_input: CodeInput):
    code = code_input.code
    language = code_input.language
    response = await service.process_execution_input(language, code)
    if response is None:
        return {"status": "Error"}
    else:
        return response.json()