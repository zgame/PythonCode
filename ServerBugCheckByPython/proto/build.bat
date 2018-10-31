
protoc -I=./ --python_out=./ CMD_Common.proto
protoc -I=./ --python_out=./ CMD_GameServer.proto
protoc -I=./ --python_out=./ CMD_GlobalServer.proto
protoc -I=./ --python_out=./ CMD_GlobalServer_Inner.proto
protoc -I=./ --python_out=./ CMD_LoginServer.proto
protoc -I=./ --python_out=./ CMD_Monitor.proto

pause