from adapter.messagingAdapter import MessagingAdapter
from adapter.webWorkerAdapter import WorkerAdapter
from adapter.queueWorkerAdapter import QueueWorkerAdapter
message_adapter = MessagingAdapter()


class GatewaySevice:
    def __init__(self, worker_adapter: WorkerAdapter, queue_adapter: QueueWorkerAdapter):
        self.worker_adapter = worker_adapter
        self.queue_adapter = queue_adapter

    async def process_execution_input(self, language: str, code: str):
        if language is None or code is None or len(language) == 0 or len(code) == 0:
            return
        try:
            print(f'DEBUG DATA: code:{code} language:{language}')
            await message_adapter.publish_message(language, code)
            response = await self.worker_adapter.execute_input(code, language)
            return response
        except Exception as e:
            print(e)
            return None

    async def schedule_execution_input(self, language: str, code:str):
        if language is None or code is None or len(language) == 0 or len(code) == 0:
            return
        try:
            print(f'DEBUG DATA: code:{code} language:{language}')
            task_id = await self.queue_adapter.schedule_exec_task(code, language)
            return {"task_id": task_id}
        except Exception as e:
            print(e)
            return None

    async def check_scheduled_task_status(self, task_id: str):
        if task_id:
            status = await self.queue_adapter.check_state_of_task_id(task_id)
            return {"status":status}
        else:
            return {"status": "Couldn't check due to invalid input."}