# http://websockets.readthedocs.io/en/stable/intro.html

import asyncio
import struct
import websockets
# from procotol.test_person import PromptForAddress
# import procotol.books_pb2 as bk
#
# import BY_proto.CMD_Common_pb2 as CommonCMD
# import BY_proto.CMD_GameServer_pb2 as GameServerCMD
# import BY_proto.CMD_GlobalServer_Inner_pb2 as GlobalServerInnerCMD
# import BY_proto.CMD_GlobalServer_pb2 as GlobalServerCMD
# import BY_proto.CMD_LoginServer_pb2 as LoginServerCMD
# import BY_proto.CMD_Monitor_pb2 as MonitorCMD


async def hello():
    async with websockets.connect('ws://172.0.0.1:8330') as websocket:
        # address1 = bk.AddressBook()
        # PromptForAddress(address1.people.add())
        # name = address1.SerializeToString()

        buffer_t = struct.pack("BBHHHH", 0, 1, 0, 1100, 10, 0)

        await websocket.send(buffer_t)
        print("> {}".format(buffer_t))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

        # address1.ParseFromString(name)
        # print(address1)


# asyncio.get_event_loop().run_until_complete(hello())


def main():
    print("---------start!---------")
    asyncio.get_event_loop().run_until_complete(hello())
    print("---------end!---------")


if __name__ == "__main__":
    main()
