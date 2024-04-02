import asyncio
from request_stream import RequestGenerator
from server1 import Server as S1
from server2 import Server as S2

class LoadBalancer:
    def __init__(self, event_generator, servers_farm, max_events_in_memory=100):
        self.event_generator = event_generator
        self.servers_farm = servers_farm
        self.event_queue = asyncio.Queue(max_events_in_memory)

    def get_server_with_least_load(self):
        loads = [s.get_current_load() for s in self.servers_farm]
        print(f"Server loads: {loads}")
        least_loaded_server = self.servers_farm[loads.index(min(loads))]
        return least_loaded_server
    
    async def enqueue_events(self):
        async for event in self.event_generator.generate_events():
            await self.event_queue.put(event)

    async def process_events(self):
        while True:
            event = await self.event_queue.get()
            chosen_server = self.get_server_with_least_load()
            asyncio.create_task(chosen_server.process_request(event))
            self.event_queue.task_done()

async def main():
    request_generator = RequestGenerator()
    server1 = S1("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)
    server2 = S2("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)
    load_balancer = LoadBalancer(request_generator, [server1, server2])
    event_producer = asyncio.create_task(load_balancer.enqueue_events())
    event_processor = asyncio.create_task(load_balancer.process_events())
    await asyncio.gather(event_producer, event_processor)

if __name__ == "__main__":
    asyncio.run(main())

    