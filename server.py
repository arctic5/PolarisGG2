from networking import buffer
from random import randint
from player import *
import socket
import constants
import time

# is there a better way to do this?
global global_players
global global_tcpListener
global global_serverSocket
global global_attemptPortForward
global global_hostingPort
global global_gg2lobbyId
global global_protocolUuid
global global_sendBuffer

global_protocolUuid = buffer.buffer_create()
buffer.parseUuid(constants.PROTOCOL_UUID, global_protocolUuid) 

global_gg2lobbyId = buffer.buffer_create()
buffer.parseUuid(constants.GG2_LOBBY_UUID, global_gg2lobbyId)

global_sendBuffer = buffer.buffer_create()

print "enter a port"
global_hostingPort = input()
global_attemptPortForward = 1

global_tcpListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendLobbyRegistration(asdf):
    lobbyBuffer = buffer.buffer_create()
    #set_little_endian(lobbyBuffer, False)
    lobbyBuffer.endianness = constants.ENDIAN_BIG
    
    buffer.parseUuid("b5dae2e8-424f-9ed0-0fcb-8c21c7ca1352", lobbyBuffer)
    buffer.write_directly_to_buffer(lobbyBuffer, asdf.serverId.bufferString)
    buffer.write_directly_to_buffer(lobbyBuffer, global_gg2lobbyId.bufferString)
    buffer.write_ubyte(lobbyBuffer, 0) # TCP
    buffer.write_ushort(lobbyBuffer, global_hostingPort) # playerLimit
    buffer.write_ushort(lobbyBuffer, 10) # noOfPlayers
    buffer.write_ushort(lobbyBuffer, 0) # Number of bots
    buffer.write_ushort(lobbyBuffer, 1) # serverPassword
    buffer.write_ushort(lobbyBuffer, 7) # Number of Key/Value pairs that follow
    buffer.writeKeyValue(lobbyBuffer, "name", "POLARIS") # serverName
    buffer.writeKeyValue(lobbyBuffer, "game", "POLARIS") #GAME_NAME_STRING
    buffer.writeKeyValue(lobbyBuffer, "game_short", "POLARIS") 
    buffer.writeKeyValue(lobbyBuffer, "game_ver", "4654765")
    buffer.writeKeyValue(lobbyBuffer, "game_url", "1337")
    buffer.writeKeyValue(lobbyBuffer, "map", "GAY_GAY")
    buffer.write_ubyte(lobbyBuffer, len("protocol_id"))
    buffer.write_string(lobbyBuffer, "protocol_id")
    buffer.write_ushort(lobbyBuffer, 16)
    buffer.write_directly_to_buffer(lobbyBuffer, global_protocolUuid.bufferString)
    #buffer.parseUuid("de7d74f8-455c-bc1b-3731-0519c44356dc", lobbyBuffer)
    lobbySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    lobbySocket.sendto(lobbyBuffer.bufferString, (constants.LOBBY_SERVER_HOST, constants.LOBBY_SERVER_PORT))
    #udp_send(lobbyBuffer, constants.LOBBY_SERVER_HOST, constants.LOBBY_SERVER_PORT)
    buffer.buffer_destroy(lobbyBuffer)

class GameServer:
    def __init__(self):
        # if (attemptPortForward == 1):
            # upnp_set_description("GG2 (TCP)")
            # discovery_error = upnp_discover(2000)
        
        # if (upnp_error_string(discovery_error) != ""):
            # print upnp_error_string(discovery_error)
        # else:
            # forwarding_error = upnp_forward_port(str(hostingPort), str(hostingPort), "TCP", "0")
            # if (upnp_error_string(forwarding_error) != ""):
                # print upnp_error_string(forwarding_error)
        global_players = []
        global_serverSocket = -1
        
        self.serverbalance=0
        self.balancecounter=0
        self.frame = 0
        self.updatePlayer = 1
        self.syncTimer = 0
        self.map_rotation = []
        
        self.serverId = buffer.buffer_create()
        for i in range(0,16):
            buffer.write_ubyte(self.serverId, randint(0,255));
            
        self.serverbalance=0
        self.balancecounter=0
        self.frame = 0
        self.updatePlayer = 1
        self.impendingMapChange = -1 
        self.syncTimer = 0; 
        
        serverPlayer = Player()
        
        serverPlayer.name = "HOST (CHANGE THIS LATER)";
        
        global_players.append(serverPlayer)
        
        global_tcpListener.bind(("127.0.0.1", global_hostingPort))
        global_tcpListener.listen(1)
        global_tcpListener.setblocking(0)
        
        self.last_sync = time.clock()
        
        print "serving on port:",global_hostingPort
        sendLobbyRegistration(self)
    def GameServerBeginStep(self):
        if (self.last_sync+30 <= time.clock()):
            sendLobbyRegistration(self)
    def GameServerEndStep(self):
        try:
            joiningSocket,joiningIP = global_tcpListener.accept()
            print "got a connection!"
            print joiningIP
            buffer.write_ubyte(global_sendBuffer, constants.KICK)
            buffer.write_ubyte(global_sendBuffer, constants.KICK_MULTI_CLIENT)
            joiningSocket.sendall(global_sendBuffer)
            joiningSocket.close()
        except:
            pass
            
        # if (joiningSocket > 0):
            # print socket_remote_ip(joiningSocket)
            # print "hi, bye"
            # buffer.write_ubyte(joiningSocket, KICK)
            # socket_send(joiningSocket)
            # socket_destroy(joiningSocket)
        # pass
        
if __name__ == '__main__':
    server = GameServer()
    while True:
        server.GameServerBeginStep()
        server.GameServerEndStep()
        time.sleep(constants.PHYSICS_TIMESTEP)