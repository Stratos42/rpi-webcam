#!/usr/bin/python
##

from twisted.protocols import basic
from twisted.web.websockets import WebSocketsResource, WebSocketsProtocol, lookupProtocolForFactory
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import protocol
from twisted.application import service, internet
from twisted.internet.protocol import Factory
from twisted.internet import task
import time, datetime, json, thread, pipan

class WebsocketChat(basic.LineReceiver):
    p = pipan.PiPan()

    def connectionMade(self):
        print "Got new client!"
	self.transport.write('connected ....\n')
	self.factory.clients.append(self)

    def connectionLost(self, reason):
        print "Lost a client!"
	self.factory.clients.remove(self)


    def dataReceived(self, data):
        if data.split(" ")[0] == "COO":
            coo = data.split(" ")[1].split("=")
            if coo[0] == "x":
                self.p.do_pan(int(coo[1]))
            if coo[0] == "y":
                self.p.do_tilt(int(coo[1]))
        self.factory.messages[float(time.time())] = data
        self.updateClients(data)

    def updateClients(self, data):
        for c in self.factory.clients:
            c.message(data)

    def message(self, message):
        self.transport.write(message + '\n')

class ChatFactory(Factory):
    protocol = WebsocketChat
    clients = []
    messages = {}

resource = WebSocketsResource(lookupProtocolForFactory(ChatFactory()))
root = Resource()
#serve chat protocol on /ws
root.putChild("ws",resource)
application = service.Application("chatserver")
#run a TCP server on port 1025, serving the chat protocol.
internet.TCPServer(1025, Site(root)).setServiceParent(application)
