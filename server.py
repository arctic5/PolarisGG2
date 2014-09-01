from ctypes import *
from forwarding import *
from faucetnet import *
from random import randint
from player import *
import uuid

gg2dll = cdll.LoadLibrary("GG2DLL.dll")

global players
global tcpListener
global serverSocket
global attemptPortForward
global hostingPort
global gg2lobbyId

gg2lobbyId = buffer_create()

hostingPort = 8190
attemptPortForward = 1

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
        players = []
        tcpListener = -1
        serverSocket = -1
        
        serverId = buffer_create()
        self.serverbalance=0
        self.balancecounter=0
        self.frame = 0
        self.updatePlayer = 1
        self.syncTimer = 0
        self.map_rotation = []
        
        for i in range(0,16):
            write_ubyte(serverId, randint(0,255));
            
        self.serverbalance=0
        self.balancecounter=0
        self.frame = 0
        self.updatePlayer = 1
        self.impendingMapChange = -1 
        self.syncTimer = 0; 
        
        serverPlayer = Player()
        
        serverPlayer.name = "HOST (CHANGE THIS LATER)";
        
        players.append(serverPlayer)
        
        tcpListener = tcp_listen(hostingPort)
        if(socket_has_error(tcpListener)==True):
            print "Unable to host:",socket_error(tcpListener)
            
        serverSocket = tcp_connect("127.0.0.1", hostingPort)
        
        if(socket_has_error(serverSocket)==True):
            print "Unable to connect to self. Epic fail, dude."
    def GameServerStep(self):
        lobbyBuffer = buffer_create();
        #TODO set_little_endian
        set_little_endian(lobbyBuffer, False)
        
        parseUuid("b5dae2e8-424f-9ed0-0fcb-8c21c7ca1352", lobbyBuffer)
        write_buffer(lobbyBuffer, 1)
        write_buffer(lobbyBuffer, gg2lobbyId)
        write_ubyte(lobbyBuffer, 0) # TCP
        write_ushort(lobbyBuffer, hostingPort)
        write_ushort(lobbyBuffer, 1337)
        write_ushort(lobbyBuffer, 1337)
        write_ushort(lobbyBuffer, 1)
        write_ushort(lobbyBuffer, 7)
        writeKeyValue(lobbyBuffer, "name", "POLARIS")
        writeKeyValue(lobbyBuffer, "game", "POLARIS")
        writeKeyValue(lobbyBuffer, "game_short", "POLARIS")
        writeKeyValue(lobbyBuffer, "game_ver", "4654765")
        writeKeyValue(lobbyBuffer, "game_url", "1337")
        writeKeyValue(lobbyBuffer, "map", "GAY_GAY")
        write_ubyte(lobbyBuffer, len("protocol_id"))
        write_string(lobbyBuffer, "protocol_id")
        write_ushort(lobbyBuffer, 16)
        write_buffer(lobbyBuffer, "de7d74f8-455c-bc1b-3731-0519c44356dc")
        
        udp_send(lobbyBuffer, "ganggarrison.com", 29944)
        buffer_destroy(lobbyBuffer)
       
        
        
if __name__ == '__main__':
    s = GameServer()
    while True:
        s.GameServerStep()