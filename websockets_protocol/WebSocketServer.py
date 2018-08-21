# # http://websockets.readthedocs.io/en/stable/intro.html
#
# #!/usr/bin/env python
#
import asyncio
import websockets
import procotol.books_pb2 as bk

async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))
    await websocket.send(name)
    print("> {}".format(name))

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

