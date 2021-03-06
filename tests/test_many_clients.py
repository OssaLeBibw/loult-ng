#!/usr/bin/env python

import os, sys

# t-thanks Python (or am I a dumb fuck?)
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import asyncio
import json
import time
import websockets

from os import urandom
from config import MAX_COOKIES_PER_IP

async def client(loop):
    ck = urandom(16).hex()
    async with websockets.connect(u"ws://127.0.0.1:80/socket/") as websocket:

        while True:
            data = await websocket.recv()
            await websocket.recv()
            if isinstance(data, str):
                print("[client {}] Message : {}".format(ck, data))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = []

    for i in range(MAX_COOKIES_PER_IP):
        task = asyncio.ensure_future(client(loop))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_forever()
    loop.close()
    
