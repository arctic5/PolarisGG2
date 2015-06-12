from faucet_networking import socket, buffer
import engine
import constants
import time

class JoiningPlayer(engineself.Entity):
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

        self.state = self.STATE_EXPECT_HELLO
        self.expectedBytes = 17
        self.lastContact = round(time.time() * 1000) # To allow implementing a timeout
        self.cumulativeMapBytes = 0
        self.states = { }

    def expect_hello(self):
        self.sameProtocol = (read_ubyte(self.sock) == constants.HELLO)
        server.protocolUuid.pos = 0
        
        for i in range(0,4):
            if (buffer.read_uint(self.sock) != read_uint(server.protocolUuid)):
                self.sameProtocol = False
        if(not self.sameProtocol):
            buffer.write_ubyte(self.sock, constants.INCOMPATIBLE_PROTOCOL)
        elif (server.password != ""):
            self.newState = self.STATE_CLIENT_AUTHENTICATED
            self.expectedBytes = 0
        else:
            buffer.write_ubyte(self.sock, constants.PASSWORD_REQUEST)
            self.newState = self.STATE_EXPECT_MESSAGELEN
            self.messageState = self.STATE_EXPECT_PASSWORD
            self.expectedBytes = 1

    def expect_messagelen():
        self.expectedBytes = buffer.read_ubyte(self.sock)
        self.newState = self.messageState

    def expect_password():
        if(buffer.read_string(self.sock, self.expectedBytes) == server.serverPassword):
            self.newState = self.STATE_CLIENT_AUTHENTICATED
            self.expectedBytes = 0
        else:
            buffer.write_ubyte(self.sock, constants.PASSWORD_WRONG)

    def client_authenticated():
        buffer.write_ubyte(self.sock, HELLO)
        buffer.write_ubyte(self.sock, len(server.serverName))
        buffer.write_string(self.sock, server.serverName)
        buffer.write_ubyte(self.sock, len(server.currentMap))
        buffer.write_string(self.sock, server.currentMap)
        buffer.write_ubyte(self.sock, len(server.currentMapMD5))
        buffer.write_string(self.sock, server.currentMapMD5)
        
        buffer.write_ubyte(self.sock, server.serverPluginsRequired)
        buffer.write_ubyte(self.sock, len(server.pluginList))
        buffer.write_string(self.sock, server.pluginList)
        
        self.advertisedMap = server.currentMap
        self.advertisedMapMd5 = server.currentMapMD5
        self.newState = self.STATE_EXPECT_COMMAND
            self.expectedBytes = 1

    def expect_command():
        # add map downloads later zzzzz
        self.b = buffer.read_ubyte(self.sock)
        if (self.b == constants.PING):
            self.newState = self.STATE_EXPECT_COMMAND
            self.expectedBytes = 1
        elif (self.b == constants.DOWNLOAD_MAP):
            pass

    def expect_name():
        self.noOfPlayers = len(server.players) - 1
        if (self.noOfPlayers >= server.playerlimit):
            buffer.write_ubyte(self.sock, constants.SERVER_FULL)
            return

    def service_player(self):
        self.newState = -1
        self.states = 
        {
            self.STATE_EXPECT_HELLO: expect_hello,
            self.STATE_EXPECT_MESSAGELEN: expect_messagelen
            self.STATE_EXPECT_NAME: expect_name
            self.STATE_EXPECT_PASSWORD: expect_password
            self.STATE_CLIENT_AUTHENTICATED: client_authenticated
            self.STATE_EXPECT_COMMAND: expect_command
            self.STATE_CLIENT_DOWNLOADING: client_downloading
        }
        self.states[self.state]

class Player(engine.Entity):
    def __init__(self):
        self.object = -1
        self.team = constants.TEAM_SPECTATOR
        # 10:08 AM - Lorgan: in java the word "clazz" is often used
        self.clazz = constants.CLASS_SCOUT
        self.sock = -1
        self.name = ""
        self.kicked = False
        self.stats = []

        # client setting stuff set to defaults
        queueJump = False
        
        # stat tracking array
        self.stats[constants.KILLS] = 0
        self.stats[constants.DEATHS] = 0
        self.stats[constants.CAPS] = 0
        self.stats[constants.ASSISTS] = 0
        self.stats[constants.DESTRUCTION] = 0
        self.stats[constants.STABS] = 0
        self.stats[constants.HEALING] = 0
        self.stats[constants.DEFENSES] = 0
        self.stats[constants.INVULNS] = 0
        self.stats[constants.BONUS] = 0
        self.stats[constants.DOMINATIONS] = 0
        self.stats[constants.REVENGE] = 0
        self.stats[constants.POINTS] = 0

        # statistic array for single life/arena
        self.roundStats[constants.KILLS] = 0
        self.roundStats[constants.DEATHS] = 0
        self.roundStats[constants.CAPS] = 0
        self.roundStats[constants.ASSISTS] = 0
        self.roundStats[constants.DESTRUCTION] = 0
        self.roundStats[constants.STABS] = 0
        self.roundStats[constants.HEALING] = 0
        self.roundStats[constants.DEFENSES] = 0
        self.roundStats[constants.INVULNS] = 0
        self.roundStats[constants.BONUS] = 0
        self.roundStats[constants.DOMINATIONS] = 0
        self.roundStats[constants.REVENGE] = 0
        self.roundStats[constants.POINTS] = 0

        timesChangedCapLimit = 0
        lastKnownx = 0
        lastKnowny = 0
        humiliated = False
        # Sentries for Engies
        sentry = -1
        # Haxxy rewards
        rewards = []
        badges = []
    def destroy(self):
        socket.socket_destroy(self.sock)
        #destroy other things here too when i implement it