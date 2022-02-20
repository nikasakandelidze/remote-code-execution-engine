from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from adapter.workerAdapter import WorkerAdapter
from adapter.serviceDiscovery import ServiceDiscovery
from core.gatewayService import GatewaySevice

app = FastAPI()


class CodeInput(BaseModel):
    code: Optional[str]
    language: Optional[str]


service_discovery = ServiceDiscovery()
worker_adatper = WorkerAdapter(service_discovery)
service = GatewaySevice(worker_adatper)


@app.post("/api/run/")
async def execute_code(code_input: CodeInput):
    code = code_input.code
    language = code_input.language
    response = await service.process_execution_input(language, code)
    if response is None:
        return {"status": "Error"}
    else:
        return response.json()