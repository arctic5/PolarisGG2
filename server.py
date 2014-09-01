from ctypes import *
from forwarding import *
from faucetnet import *
from random import randint
import player

gg2dll = cdll.LoadLibrary("GG2DLL.dll")

global players
global tcpListener
global serverSocket
global attemptPortForward
global hostingPort

hostingPort = 8090
attemptPortForward = 1

class Gameserver:
    def __init__(self):
        if (attemptPortForward == 1):
        upnp_set_description("GG2 (TCP)")
        discovery_error = upnp_discover(2000)
        
        if (upnp_error_string(discovery_error) != ""):
            print upnp_error_string(discovery_error)

        players = []
        tcpListener = -1
        serverSocket = -1
        
        self.serverId = buffer_create()
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
        
        global tcpListener
        
        tcpListener = tcp_listen(hostingPort)
        
        if(socket_has_error(global.tcpListener)):
            print "Unable to host:",socket_error(tcpListener)
            
        serverSocket = tcp_connect("127.0.0.1", global.hostingPort)
        
        if(socket_has_error(serverSocket)):
            print "Unable to connect to self. Epic fail, dude."
    def GameServerStep:
        
            
            