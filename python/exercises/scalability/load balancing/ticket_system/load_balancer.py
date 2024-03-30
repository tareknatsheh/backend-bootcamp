import asyncio
from request_stream import RequestGenerator
from server1 import Server as S1
from server2 import Server as S2

class LoadBalancer:
    def __init__(self, event_generator, servers_farm, max_concurrent_events=10):
        self.event_generator = event_generator
        self.servers_farm = servers_farm
        ### looks chatgpt-ish
        self.event_queue = asyncio.Queue(max_concurrent_events)  # Limit the number of events being processed concurrently
    ### why make this function async?
    async def get_server_with_least_load(self, servers: list):
        loads = [s.get_current_load() for s in servers]
        print(f"Server loads: {loads}")  # Debugging: Print current loads
        least_loaded_server = servers[loads.index(min(loads))]
        return least_loaded_server


    async def process_event(self):
        while True:
            event = await self.event_queue.get()
            handling_server = await self.get_server_with_least_load(self.servers_farm)
            await handling_server.process_request(event)
            self.event_queue.task_done()

    async def produce_events(self):
        for event in self.event_generator.generate_events():
            await self.event_queue.put(event)  # Place the event in the queue to be processed

    async def process_events(self):
        # Start event processing tasks
        tasks = [asyncio.create_task(self.process_event()) for _ in range(len(self.servers_farm))]
        producer_task = asyncio.create_task(self.produce_events())  # Start event production task
        
        await asyncio.gather(producer_task)  # Wait for the producer task to finish
        await self.event_queue.join()  # Wait for all items in the queue to be processed

        for task in tasks:
            task.cancel()  # Cancel processing tasks after all events have been processed

# Example usage:
if __name__ == "__main__":
    request_generator = RequestGenerator()
    ### this is hardcoded with magic numbers
    server1 = S1("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)
    server2 = S2("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)
    
    load_balancer = LoadBalancer(request_generator, [server1, server2])
    asyncio.run(load_balancer.process_events())
