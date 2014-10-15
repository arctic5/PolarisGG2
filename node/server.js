/// <reference path="node.d.ts" />
var net = require('net');

var GameServer = (function () {
    function GameServer() {
        this.sendBuffer = new Buffer(16);
    }
    GameServer.prototype.createServer = function (hostngPort) {
        this.tcpListener = net.createServer(function (socket) {
            // create connection handlers or something
            socket.on('data', function (data) {
                console.log('got %d bytes of data', data.length);
                var message = data.toString();
                //socket.write(message);
            });
            socket.on('close', function () {
                console.log('client disconnect');
            });
            socket.on('error', function () {
                console.log('some sort of error');
            });
        });

        this.tcpListener.listen(hostngPort, '127.0.0.1');
    };
    GameServer.prototype.accecptJoiningPlayer = function () {
        this.tcpListener.on('connection', function (socket) {
            this.sendBuffer.writeUInt8(37, 0);
            socket.write(this.sendBuffer);
        });
    };
    return GameServer;
})();

var server = new GameServer();
server.createServer(8190);
server.accecptJoiningPlayer();
