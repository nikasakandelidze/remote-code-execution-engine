import httpx

from adapter.serviceDiscovery import ServiceDiscovery
from adapter.messagingAdapter import MessagingAdapter

service_discovery = ServiceDiscovery()
message_adapter = MessagingAdapter()
PATH = "/execute/"


class GatewaySevice:
    def __init__(self):
        pass


    async def process_execution_input(self, language: str, code: str):
        if language is None or code is None or len(language) == 0 or len(code) == 0:
            return
        try:
            await message_adapter.publish_message(language, code)
            ip = service_discovery.get_next_worker_ip()
            print(f'Worker IP: {ip}{PATH}')
            print(f'DEBUG DATA: code:{code} language:{language}')
            response = httpx.post(f'{ip}{PATH}', json={'code': code, 'language': language})
            return response
        except Exception as e:
            print(e)
            return None