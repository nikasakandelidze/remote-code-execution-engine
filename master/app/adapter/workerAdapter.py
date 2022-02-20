import httpx

from adapter.serviceDiscovery import ServiceDiscovery

PATH = "/execute/"


class WorkerAdapter:
    def __init__(self, service_discovery: ServiceDiscovery):
        self.service_discovery = service_discovery
        self.client = httpx.AsyncClient()

    async def execute_input(self, code: str = "", language: str = ""):
        if len(code) == 0 or len(language) == 0:
            return None
        else:
            ip = self.service_discovery.get_next_worker_ip()
            print(f'Worker IP: {ip}{PATH}')
            response = await self.client.post(f'{ip}{PATH}', json={'code': code, 'language': language})
            return response
