import time
import warnings

import aiofiles

warnings.filterwarnings("ignore")
import asyncio
import aiohttp




async def fetch_and_save_async(session, user_id):
    print(f"Fetching user {user_id}...")
    # NON-BLOCKING: control returns to the event loop while waiting on the network
    async with session.get(f"https://jsonplaceholder.typicode.com/users/{user_id}") as response:
        data = await response.text()
        print(data)

    print(f"Saving user {user_id}...")
    # NON-BLOCKING: control returns to the event loop while waiting on disk I/O
    async with aiofiles.open(f"user_{user_id}.json", "w") as f:
        await f.write(data)


async def main_async():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_save_async(session, user_id) for user_id in range(1, 4)]
        await asyncio.gather(*tasks)
    print(time.time() - start) #Takes 0.2768559455871582

asyncio.run(main_async())