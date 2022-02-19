from typing import Optional
import httpx

from fastapi import FastAPI
from pydantic import BaseModel

from adapter.serviceDiscovery import ServiceDiscovery

app = FastAPI()

service_discovery = ServiceDiscovery()


class CodeInput(BaseModel):
    code: Optional[str]
    language: Optional[str]


PATH = "/execute/"


@app.post("/api/run/")
async def execute_code(code_input: CodeInput):
    code = code_input.code
    language = code_input.language
    try:
        ip = service_discovery.get_next_worker_ip()
        print(f'Worker IP: {ip}{PATH}')
        print(f'DEBUG DATA: code:{code} language:{language}')
        response = httpx.post(f'{ip}{PATH}', json={'code': code, 'language': language})
        return response.json()
    except Exception:
        print('Problem on master server.')
        return {'status': 'error'}