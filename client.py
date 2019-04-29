"""The most basic chat protocol possible.

run me with twistd -y chatserver.py, and then connect with multiple
telnet clients to port 1025
"""
from __future__ import print_function

from twisted.protocols import basic


global x
x = 1

class MyChat(basic.LineReceiver):
    def connectionMade(self):
        self.factory.clients.append(self)    	

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        global x
        x += 1
        for c in self.factory.clients:
        	if c != self:
        		c.message(str(x))

    def message(self, message):
    	self.transport.write(message.encode() + b'\n')


from twisted.internet import protocol
from twisted.application import service, internet

factory = protocol.ServerFactory()
factory.protocol = MyChat
factory.clients = []

application = service.Application("chatserver")
internet.TCPServer(1025, factory).setServiceParent(application)
