from networking import buffer
from random import randint
import player
import socket
import constants
import time
import sys

# is there a better way to do this?
global global_attemptPortForward

print "enter a port"
hostingPort = input()
global_attemptPortForward = 1

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
        self.tcpListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.protocolUuid = buffer.buffer_create()
        buffer.parseUuid(constants.PROTOCOL_UUID, self.protocolUuid) 

        self.gg2lobbyId = buffer.buffer_create()
        buffer.parseUuid(constants.GG2_LOBBY_UUID, self.gg2lobbyId)
        
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
        self.players = []
        serverPlayer = player.Player()
        serverPlayer.name = "HOST (CHANGE THIS LATER)";
        self.players.append(serverPlayer)
        
        # networking stuff
        self.hostingPort = port
        try:
            self.tcpListener.bind(("127.0.0.1", hostingPort))
            self.tcpListener.listen(1)
            self.tcpListener.setblocking(0)
        except socket.error, (value,message): 
            if (self.tcpListener):
                self.tcpListener.close()
            print "Could not open socket: " + message 
            sys.exit(1)
        self.tcpListener.setblocking(False)
        self.sendBuffer = buffer.buffer_create()
        
        self.last_sync = time.clock()
        
        print "serving on port:",self.hostingPort
        self.firstSend = -1
    def GameServerBeginStep(self):
        # if (self.last_sync+45 <= time.clock()):
            # lobby.sendLobbyRegistration(self)
        pass
    def GameServerEndStep(self):
        # if (self.firstSend == -1):
            # time.sleep(10)
            # lobby.sendLobbyRegistration(self)
        try:
            self.joiningSocket, self.joiningIP = self.tcpListener.accept()
            print "got a connection from", self.joiningIP[0]
            try:
                buffer.write_ubyte(self.sendBuffer, 37)
                print self.sendBuffer.bufferString
                self.data = self.joiningSocket.recv(1024)
                self.joiningSocket.sendall(self.sendBuffer.bufferString)
                self.joiningSocket.close()
                buffer.buffer_clear(self.sendBuffer)
            except:
                pass
        except:
            pass
            # no connection
if __name__ == '__main__':
    server = GameServer(hostingPort)
    while True:
        server.GameServerBeginStep()
        server.GameServerEndStep()
        #time.sleep(constants.PHYSICS_TIMESTEP)