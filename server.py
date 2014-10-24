from networking import buffer, lobby, tcp
from random import randint
from engine import player
from faucetnet import *
import socket
import constants
import time
import sys

# is there a better way to do this?

print "enter a port"
hostingPort = input()
global_attemptPortForward = 1

class JoiningPlayer:
    def __init__(self):
        self.sock = -1
        self.mapDownloadBuffer = -1

        self.STATE_EXPECT_HELLO = 1 # Hello message: 17 bytes (HELLO+UUID)
        self.STATE_EXPECT_MESSAGELEN = 2 # 1 byte Message length header 
        self.STATE_EXPECT_NAME = 3
        self.STATE_EXPECT_PASSWORD = 4
        self.STATE_CLIENT_AUTHENTICATED = 5
        self.STATE_EXPECT_COMMAND = 6
        self.STATE_CLIENT_DOWNLOADING = 7

        self.state = STATE_EXPECT_HELLO
        self.expectedBytes = 17
        self.lastContact = round(time.time() * 1000) # To allow implementing a timeout
        self.cumulativeMapBytes = 0
    def service_player(self):
        self.newState = -1;
        if (self.state == self.STATE_EXPECT_HELLO):
            self.sameProtocol = (read_ubyte(self.sock) == constants.HELLO);
            server.protocolUuid.pos = 0
            
            for i in range(0,4):
                if (read_uint(self.sock) != read_uint(server.protocolUuid)):
                    self.sameProtocol = False
            if(not self.sameProtocol):
                write_ubyte(self.sock, constants.INCOMPATIBLE_PROTOCOL);
            elif (server.password != ""):
                self.newState = self.STATE_CLIENT_AUTHENTICATED
                self.expectedBytes = 0
            else:
                write_ubyte(self.sock, constants.PASSWORD_REQUEST);
            # OK THIS IS WHERE I LEFT OFF WHEN I LAST DID SOMETHING
class GameServer:
    def __init__(self, port):
        # if (attemptPortForward == 1):
            # upnp_set_description("GG2 (TCP)")
            # discovery_error = upnp_discover(2000)
        
        # if (upnp_error_string(discovery_error) != ""):
            # print upnp_error_string(discovery_error)
        # else:
            # forwarding_error = upnp_forward_port(str(hostingPort), str(hostingPort), "TCP", "0")
            # if (upnp_error_string(forwarding_error) != ""):
                # print upnp_error_string(forwarding_error)
                
        # server vars
        self.tcpListener = tcp_listen(port)
        self.protocolUuid = buffer_create()
        buffer.parseUuid(constants.PROTOCOL_UUID, self.protocolUuid) 

        self.gg2lobbyId = buffer_create()
        buffer.parseUuid(constants.GG2_LOBBY_UUID, self.gg2lobbyId)
        
        self.serverbalance=0
        self.balancecounter=0
        self.frame = 0
        self.updatePlayer = 1
        self.syncTimer = 0
        self.map_rotation = []
        self.serverId = buffer_create()
        for i in range(0,16):
            write_ubyte(self.serverId, randint(0,255));
        self.serverbalance=0
        self.balancecounter=0
        self.frame = 0
        self.updatePlayer = 1
        self.impendingMapChange = -1 
        self.syncTimer = 0; 
        self.players = []
        serverPlayer = player.Player()
        serverPlayer.name = "HOST (CHANGE THIS LATER)";
        self.players.append(serverPlayer)
        self.password = ""
        
        # networking stuff
        self.hostingPort = port
        self.sendBuffer = buffer_create()
        self.last_sync = time.clock()
        
        print "serving on port:",self.hostingPort
        self.firstSend = -1
    def accecpt_player(self):
        self.joiningSocket = socket_accept(self.tcpListener)
        self.ip = socket_remote_ip(self.joiningSocket)
        
        self.joiningPlayer = JoiningPlayer()
        self.joiningPlayer.sock = self.joiningSocket
    def GameServerBeginStep(self):
        if (self.last_sync+45 <= time.clock()):
            lobby.sendLobbyRegistration(self)
    def GameServerEndStep(self):
        if (self.firstSend == -1):
            #TODO THIS IS A DEBUG THING REMOVE LATER
            time.sleep(10)
            lobby.sendLobbyRegistration(self)
        try:
            accecpt_player()
            with(JoiningPlayer):
                service_player()
        except:
            pass
            # no connection
if __name__ == '__main__':
    global server = GameServer(hostingPort)
    while True:
        t0 = time.clock()
        server.GameServerBeginStep()
        server.GameServerEndStep()
        time.sleep(PHYSICS_TIMESTEP)
        t1 = time.clock()