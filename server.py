from faucet_networking import buffer, socket
from random import randint
import constants
import engine
import parseUuid


# is there a better way to do this?

print "enter a port"
hostingPort = input()
global_attemptPortForward = 1

class GameServer(engine.Entity):
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
        self.tcpListener = socket.tcp_listen(port)
        self.protocolUuid = buffer.buffer_create()
        parseUuid.parseUuid(constants.PROTOCOL_UUID, self.protocolUuid) 

        self.gg2lobbyId = buffer_create()
        parseUuid.parseUuid(constants.GG2_LOBBY_UUID, self.gg2lobbyId)
        
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
    def begin_step(self):
        if (self.last_sync+45 <= time.clock()):
            lobby.sendLobbyRegistration(self)
    def end_step(self):
        if (self.firstSend == -1):
            lobby.sendLobbyRegistration(self)
        try:
            accecpt_player()
            with(JoiningPlayer):
                service_player()
        except:
            pass
            # no connection
    def ServerChangeMap():
        
    def ServerJoinUpdate(self, sock):
        buffer.write_ubyte(sock, constants.JOIN_UPDATE)
        buffer.write_ubyte(sock, len(self.players))
        buffer.write_ubyte(sock, self.currentMapArea)

        ServerChangeMap(self.currentMap, self.currentMapMD5, sock)

        for (i in players):
            ServerPlayerJoin(player.name, sock);
            ServerPlayerChangeclass(i, player.clazz, argument0);
            ServerPlayerChangeteam(i, player.team, argument0);

global server = GameServer()