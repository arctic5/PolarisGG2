/// <reference path="node.d.ts" />
import net = require('net');
import buffer = require('buffer');

class GameServer {
    tcpListener: any;
    sendBuffer: any;
    constructor() {
        this.sendBuffer = new Buffer(16);
    }
    createServer(hostngPort: number) {
        this.tcpListener = net.createServer(function(socket){
            // create connection handlers or something
            socket.on('data', function (data) {
                console.log('got %d bytes of data', data.length);
                var message: string = data.toString();
                //socket.write(message);
            });
            socket.on('close', function() {
                console.log('client disconnect');
            });
            socket.on('error', function() {
                console.log('some sort of error');
            });
        });
        
        this.tcpListener.listen(hostngPort, '127.0.0.1');
    }
    accecptJoiningPlayer() {
        this.tcpListener.on('connection', function (socket) {
            this.sendBuffer.writeUInt8(37, 0);
            socket.write(this.sendBuffer);
        });
    }
}

var server = new GameServer();
server.createServer(8190);
server.accecptJoiningPlayer();