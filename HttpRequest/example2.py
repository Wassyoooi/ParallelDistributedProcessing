# Example 2: asynchronous requests
import asyncio
import requests
import time

start = 0

async def main():
    start = time.time()

    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None, 
            requests.get, 
            'https://ie.u-ryukyu.ac.jp/'
        )
        for i in range(20)
    ]
    for response in await asyncio.gather(*futures):
        print(time.time() - start)
        pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
