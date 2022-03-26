import asyncio

from celery import Celery
import celery.states as states


celery = Celery("code_execution_worker")
celery.conf.broker_url="amqp://guest:guest@mqueue:5672/"
celery.conf.result_backend="redis://redis:6379"


class QueueWorkerAdapter:
    async def schedule_exec_task(self, code: str = "", language: str = ""):
        if len(code) == 0 or len(language) == 0:
            return None
        else:
            task = celery.send_task("execute_code_task", args=[code, language])
            return task.id


    async def check_state_of_task_id(self, id):
        res = celery.AsyncResult(id)
        return res.state if res.state == states.PENDING else str(res.result)