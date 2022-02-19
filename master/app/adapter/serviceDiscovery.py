PROTOCOL ='http'
COMMON_HOST = 'worker'


class ServiceDiscovery:
    def __init__(self):
        self.worker_ips=[f'{PROTOCOL}://{COMMON_HOST}1:80', f'{PROTOCOL}://{COMMON_HOST}2:81', f'{PROTOCOL}://{COMMON_HOST}3:82']
        self.round_robin_counter = 0

    def get_next_worker_ip(self):
        index = self.round_robin_counter % len(self.worker_ips)
        self.round_robin_counter += 1
        return self.worker_ips[index]