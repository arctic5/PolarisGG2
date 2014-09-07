from forwarding import *
from faucetnet import *
from random import randint
from player import *
from ctypes import *
import constants



#gg2dll = cdll.LoadLibrary("GG2DLL.dll")

global players
global tcpListener
global serverSocket
global attemptPortForward
global hostingPort
global gg2lobbyId
global protocolUuid

protocolUuid = buffer_create()
#parseUuid(constants.PROTOCOL_UUID, protocolUuid) 

gg2lobbyId = buffer_create()
#parseUuid(constants.GG2_LOBBY_UUID, gg2lobbyId)

hostingPort = 8190
attemptPortForward = 1

tcpListener = tcp_listen(hostingPort)

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
        # players = []
        # serverSocket = -1
        
        # serverId = buffer_create()
        # self.serverbalance=0
        # self.balancecounter=0
        # self.frame = 0
        # self.updatePlayer = 1
        # self.syncTimer = 0
        # self.map_rotation = []
        
        # for i in range(0,16):
            # write_ubyte(serverId, randint(0,255));
            
        # self.serverbalance=0
        # self.balancecounter=0
        # self.frame = 0
        # self.updatePlayer = 1
        # self.impendingMapChange = -1 
        # self.syncTimer = 0; 
        
        # serverPlayer = Player()
        
        # serverPlayer.name = "HOST (CHANGE THIS LATER)";
        
        # players.append(serverPlayer)
        
        ttcpListener = c_double(1)
        
        print ttcpListener
        # print type(ttcpListener)
        # if(socket_has_error(tcpListener)):
            # print "Unable to host:",socket_error(tcpListener)
            
        # print socket_error(tcpListener)
            
        # print "serving on port:",hostingPort
    # def GameServerBeginStep(self):
        # lobbyBuffer = buffer_create()
        # set_little_endian(lobbyBuffer, False)
        
        # parseUuid("b5dae2e8-424f-9ed0-0fcb-8c21c7ca1352", lobbyBuffer)
        # write_buffer(lobbyBuffer, 1)
        # write_buffer(lobbyBuffer, gg2lobbyId)
        # write_ubyte(lobbyBuffer, 0) # TCP
        # write_ushort(lobbyBuffer, hostingPort) # playerLimit
        # write_ushort(lobbyBuffer, 1337) # noOfPlayers
        # write_ushort(lobbyBuffer, 1337) # Number of bots
        # write_ushort(lobbyBuffer, 1) # serverPassword
        # write_ushort(lobbyBuffer, 7) # Number of Key/Value pairs that follow
        # writeKeyValue(lobbyBuffer, "name", "POLARIS") # serverName
        # writeKeyValue(lobbyBuffer, "game", "POLARIS") #GAME_NAME_STRING
        # writeKeyValue(lobbyBuffer, "game_short", "POLARIS") 
        # writeKeyValue(lobbyBuffer, "game_ver", "4654765")
        # writeKeyValue(lobbyBuffer, "game_url", "1337")
        # writeKeyValue(lobbyBuffer, "map", "GAY_GAY")
        # write_ubyte(lobbyBuffer, len("protocol_id"))
        # write_string(lobbyBuffer, "protocol_id")
        # write_ushort(lobbyBuffer, 16)
        # parseUuid("de7d74f8-455c-bc1b-3731-0519c44356dc", lobbyBuffer)
        
        # udp_send(lobbyBuffer, constants.LOBBY_SERVER_HOST, constants.LOBBY_SERVER_PORT)
        # buffer_destroy(lobbyBuffer)
    # def GameServerEndStep(self):
        # joiningSocket = socket_accept(tcpListener)
        # if (joiningSocket > 0):
            # print socket_remote_ip(joiningSocket)
            # print "hi, bye"
            # write_ubyte(joiningSocket, KICK)
            # socket_send(joiningSocket)
            # socket_destroy(joiningSocket)
        
        
if __name__ == '__main__':
    server = GameServer()
    # while True:
        # server.GameServerBeginStep()
        # server.GameServerEndStep()