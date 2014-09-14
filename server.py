from networking import buffer, tcp, lobby
from random import randint
import player
import socket
import constants
import time

# is there a better way to do this?
global global_attemptPortForward



global_sendBuffer = buffer.buffer_create()

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
        self.tcpListener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpListener.bind(("", port))
        self.tcpListener.listen(10)
        self.tcpListener.setblocking(False)
        self.sendbuffer = []
        
        self.last_sync = time.clock()
        
        print "serving on port:",port
        lobby.sendLobbyRegistration(self)
    def GameServerBeginStep(self):
        if (self.last_sync+45 <= time.clock()):
            lobby.sendLobbyRegistration(self)
    def GameServerEndStep(self):
        try:
            self.joiningSocket, self.joiningIP = global_tcpListener.accept()
            print "got a connection from", self.joiningIP[0]
            buffer.write_ubyte(self.sendBuffer, constants.KICK)
            #buffer.write_ubyte(global_sendBuffer, constants.KICK_MULTI_CLIENT)
            try:
                self.joiningSocket.send(self.sendBuffer.bufferString)
                tcp.socket_send(self.joiningSocket, self.sendBuffer)
            except:
                print self.joiningSocket.error
            print "CLIENT KICKED"
            time.sleep(1)
            print "CLIENT SENT:", self.joiningSocket.recv(constants.MAX_PACKET_SIZE)
            self.joiningSocket.close()
        except:
            pass
        
if __name__ == '__main__':
    server = GameServer(hostingPort)
    while True:
        server.GameServerBeginStep()
        server.GameServerEndStep()
        time.sleep(constants.PHYSICS_TIMESTEP)