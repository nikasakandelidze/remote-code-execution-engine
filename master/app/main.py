import json

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from adapter.webWorkerAdapter import WorkerAdapter
from adapter.serviceDiscovery import ServiceDiscovery
from core.gatewayService import GatewaySevice
from adapter.queueWorkerAdapter import QueueWorkerAdapter

app = FastAPI()


class CodeInput(BaseModel):
    code: Optional[str]
    language: Optional[str]


service_discovery = ServiceDiscovery()
worker_adatper = WorkerAdapter(service_discovery)
queue_worker_adapter = QueueWorkerAdapter()
service = GatewaySevice(worker_adatper, queue_worker_adapter)


@app.post("/api/run/")
async def execute_code(code_input: CodeInput):
    code = code_input.code
    language = code_input.language
    response = await service.process_execution_input(language, code)
    if response is None:
        return {"status": "Error"}
    else:
        return response.json()


@app.post("/api/schedule/")
async def execute_code(code_input: CodeInput):
    code = code_input.code
    language = code_input.language
    response = await service.schedule_execution_input(language, code)
    if response is None:
        return {"status": "Error"}
    else:
        return response


@app.get("/api/schedule/check/{id}")
async def execute_code(id: str):
    print(f"Input id of check scheduled task is: {id} ")
    response = await service.check_scheduled_task_status(id)
    print(f"Response to check task is: {response}")
    if response is None:
        return {"status": "Error"}
    else:
        return response