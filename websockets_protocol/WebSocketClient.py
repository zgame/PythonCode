# http://websockets.readthedocs.io/en/stable/intro.html

import asyncio
import websockets
from procotol.test_person import PromptForAddress
import procotol.books_pb2 as bk

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        address1 = bk.AddressBook()
        PromptForAddress(address1.people.add())
        name = address1.SerializeToString()
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

        address1.ParseFromString(name)
        print(address1)


asyncio.get_event_loop().run_until_complete(hello())
