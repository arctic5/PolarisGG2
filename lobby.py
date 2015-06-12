from faucet_networking import *
import time
import random

def writeKeyValue(buffer, key, value):
    if(len(key) > 255)
        print "Key too long: " + key
        return -1
    if(len(value) > 65535)
        value = value[:65535]
    write_ubyte(buffer, len(key))
    write_string(buffer, key)
    write_ushort(buffer, len(value))
    write_string(buffer, value)


def sendLobbyRegistration(server):
    lobbyBuffer = buffer_create()
    set_little_endian(lobbyBuffer, False)
    lobbyBuffer.endianness = constants.ENDIAN_BIG
    
    parseUuid("b5dae2e8-424f-9ed0-0fcb-8c21c7ca1352", lobbyBuffer)
    write_buffer(lobbyBuffer, server.serverId)
    write_buffer(lobbyBuffer, server.gg2lobbyId)
    write_ubyte(lobbyBuffer, 0) # TCP
    write_ushort(lobbyBuffer, server.hostingPort) # port
    write_ushort(lobbyBuffer, 1337) # player cap
    write_ushort(lobbyBuffer, 0) #number of players
    write_ushort(lobbyBuffer, 0) # bots
    write_ushort(lobbyBuffer, 0) #password
    write_ushort(lobbyBuffer, 7) # Number of Key/Value pairs that follow
    writeKeyValue(lobbyBuffer, "name", "a distant star") # serverName
    writeKeyValue(lobbyBuffer, "game", "PolarisGG2") #GAME_NAME_STRING
    writeKeyValue(lobbyBuffer, "game_short", "star") # short name
    writeKeyValue(lobbyBuffer, "game_ver", "1337") # version string
    writeKeyValue(lobbyBuffer, "game_url", "https://www.youtube.com/watch?v=dQw4w9WgXcQ") # url string
    writeKeyValue(lobbyBuffer, "map", "gay_garrison_2") # map
    write_ubyte(lobbyBuffer, len("protocol_id")) 
    write_string(lobbyBuffer, "protocol_id")
    write_ushort(lobbyBuffer, 16)
    write_buffer(lobbyBuffer, server.protocolUuid)
    udp_send(lobbyBuffer, constants.LOBBY_SERVER_HOST, constants.LOBBY_SERVER_PORT);
    print "sent registration"
    server.last_sync = time.clock()
    buffer_destroy(lobbyBuffer)
    lobbySocket.close()