import sys
sys.path.append("../")
import constants
import buffer
import socket
import time
import random

def sendLobbyRegistration(server):
    lobbyBuffer = buffer.buffer_create()
    #set_little_endian(lobbyBuffer, False)
    lobbyBuffer.endianness = constants.ENDIAN_BIG
    
    buffer.parseUuid("b5dae2e8-424f-9ed0-0fcb-8c21c7ca1352", lobbyBuffer)
    buffer.write_directly_to_buffer(lobbyBuffer, server.serverId.bufferString)
    buffer.write_directly_to_buffer(lobbyBuffer, server.gg2lobbyId.bufferString)
    buffer.write_ubyte(lobbyBuffer, 0) # TCP
    buffer.write_ushort(lobbyBuffer, server.hostingPort) # port
    buffer.write_ushort(lobbyBuffer, 1337) # player cap
    buffer.write_ushort(lobbyBuffer, 0) #number of players
    buffer.write_ushort(lobbyBuffer, 0) # bots
    buffer.write_ushort(lobbyBuffer, 0) #password
    buffer.write_ushort(lobbyBuffer, 7) # Number of Key/Value pairs that follow
    buffer.writeKeyValue(lobbyBuffer, "name", "a distant star") # serverName
    buffer.writeKeyValue(lobbyBuffer, "game", "PolarisGG2") #GAME_NAME_STRING
    buffer.writeKeyValue(lobbyBuffer, "game_short", "star") # short name
    buffer.writeKeyValue(lobbyBuffer, "game_ver", "1337") # version string
    buffer.writeKeyValue(lobbyBuffer, "game_url", "https://www.youtube.com/watch?v=dQw4w9WgXcQ") # url string
    buffer.writeKeyValue(lobbyBuffer, "map", "gay_garrison_2") # map
    buffer.write_ubyte(lobbyBuffer, len("protocol_id")) 
    buffer.write_string(lobbyBuffer, "protocol_id")
    buffer.write_ushort(lobbyBuffer, 16)
    buffer.write_directly_to_buffer(lobbyBuffer, server.protocolUuid.bufferString)
    lobbySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    lobbySocket.sendto(lobbyBuffer.bufferString, (constants.LOBBY_SERVER_HOST, constants.LOBBY_SERVER_PORT))
    print "sent registration"
    server.last_sync = time.clock()
    buffer.buffer_destroy(lobbyBuffer)