from adapter.messagingAdapter import MessagingAdapter
from adapter.workerAdapter import WorkerAdapter

message_adapter = MessagingAdapter()


class GatewaySevice:
    def __init__(self, worker_adapter: WorkerAdapter ):
        self.worker_adapter = worker_adapter

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