import json
import time
import asyncio

class FileSystem:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_json_db(self) -> dict:
        with open(self.file_path, 'r') as f:
            return json.load(f)
    
    async def update_json_db(self, updated_data) -> bool:
        # keep trying to access until success
        while True:
            try:
                myfile = open(self.file_path, "r+")
                break
            except IOError:
                print("Could not open db file! will try again in half a second.")
                await asyncio.sleep(0.5)
                # restart the loop
        try:
            with myfile as f:
                f.seek(0)
                json.dump(updated_data,f, indent=4, sort_keys=True)
                f.truncate()
                return True
        except Exception:
            return False


class Server:
    def __init__(self, tickets_file, max_requests_per_time=5, requests_threshold_delay=2, max_concurrent_requests=3):
        self.fs = FileSystem(tickets_file)
        self.tickets_db = self.fs.get_json_db()
        self.requests_count = 0
        self.requests_time = time.time()
        self.max_requests_per_time = max_requests_per_time
        self.requests_threshold_delay = requests_threshold_delay
        self.max_concurrent_requests = max_concurrent_requests
        self.current_concurrent_requests = 0

    def sell_ticket(self, event) -> bool:
        if event not in self.tickets_db or self.tickets_db[event] <= 0:
            print(f"No tickets available for {event}.")
            return False
        if self.current_concurrent_requests >= self.max_concurrent_requests:
            raise Exception("Server overloaded. Please try again later.")
        
        self.tickets_db[event] -= 1
        print(f"Sold 1 ticket for {event}. Remaining: {self.tickets_db[event]}")
        return True

    def show_unsold_tickets(self):
        print("Unsold tickets:")
        for event, tickets in self.tickets_db.items():
            if tickets > 0:
                print(f"{event}: {tickets} tickets available.")

    async def process_request(self, event) -> bool:
        print("Server 2 is handling")
        self.current_concurrent_requests += 1
        # Check if the number of requests exceeds the threshold
        self.requests_count += 1
        if self.requests_count > self.max_requests_per_time:
            current_time = time.time()
            elapsed_time = current_time - self.requests_time
            if elapsed_time < 10:  # Y time unit (adjust as needed)
                print("Too many requests. Delaying response.")
                await asyncio.sleep(self.requests_threshold_delay)
            else:
                self.requests_time = current_time
                self.requests_count = 1
        # Simulate processing time
        await asyncio.sleep(0.5)
        
        sell_result: bool = self.sell_ticket(event["event"])
        
        if sell_result:
            # update db
            update_status = await self.fs.update_json_db(self.tickets_db)
            self.current_concurrent_requests -= 1
            return update_status
        else:
            return sell_result
    
    def get_current_load(self) -> float:
        return self.current_concurrent_requests / self.max_concurrent_requests
            
            

# Example usage:
if __name__ == "__main__":
    server = Server("tickets.json", max_requests_per_time=10, requests_threshold_delay=3, max_concurrent_requests=5)
    