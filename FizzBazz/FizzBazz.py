# -*- coding: utf-8 -*-
# from asyncio import Queue
# from queue import Queue
import asyncio

def fizzbuzz(i):
    if i == 15:
        return 'FizzBuzz'
    if i % 5 == 0:
        return 'Buzz'
    if i % 3 == 0:
        return 'Fizz'
    return str(i)

async def task_fizzbuzz(prefix):
    for x in range(1, 10):
        # await asyncio.sleep(1)
        print(prefix + "{}:".format(str(x)) + fizzbuzz(x))
    return None

loop = asyncio.get_event_loop()
# コルーチン1000個生成
tasks = asyncio.wait([task_fizzbuzz(str(i) + ":") for i in range(1, 1000)])
loop.run_until_complete(tasks)
loop.close()

