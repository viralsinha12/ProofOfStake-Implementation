"""The most basic chat protocol possible.

run me with twistd -y chatserver.py, and then connect with multiple
telnet clients to port 1025
"""

from __future__ import print_function

from twisted.protocols import basic

class Transaction:

    def __init__(self,transactionId, timeStamp,inputCounter,outputCounter,blockTimeStamp,confirmations):
        self.transactionId = transactionId
        # transaction timestamp
        self.timeStamp = timeStamp
        #number of inputs - single/split
        self.inputCounter = inputCounter
        #return value or not
        self.outputCounter = outputCounter
        #Class objects
        # ValueIn valueIn
        # ValueOut valuesOut
        self.blockTimeStamp = blockTimeStamp
        #how many people have confirmed this transactions - ?!?!
        self.confirmations = confirmations



# class ValueIn:
#     previousTransactionId
#     sendersAddress
#     amount

# class ValueOut:
#     receiverAddress
#     amount

# class Block:
#     #block creation time
#     timeStamp
#     numberOfTransactions
#     #how many people have confirmed this block - ?!?!
#     confirmations
#     previousBlockHash
#     blockModifier
#     listOfTransactions
#     nonce
#     merkleRootHash
#     difficulty

import random
import datetime

# transactionId, timeStamp,inputCounter,outputCounter,blockTimeStamp,confirmations
now = datetime.datetime.now()
transactionObj1 = Transaction(random.random(),now,1,1,None,0)
now = datetime.datetime.now()
transactionObj2 = Transaction(random.random(),now,2,2,None,0)
now = datetime.datetime.now()
transactionObj3 = Transaction(random.random(),now,3,3,None,0)
now = datetime.datetime.now()
transactionObj4 = Transaction(random.random(),now,4,4,None,0)
now = datetime.datetime.now()
transactionObj5 = Transaction(random.random(),now,1,1,None,0)

global x
x = 0

class MyChat(basic.LineReceiver):

    def __init(self,value):
        self.value = value

    def connectionMade(self):
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        global x
        x += 1
        if x < 5:
            self.value = line

        for c in self.factory.clients:
            if c == self:
                c.message(str(transactionObj1.inputCounter))
                c.message(str(transactionObj2.inputCounter))
                c.message(str(transactionObj3.inputCounter))
                c.message(str(transactionObj4.inputCounter))
                c.message(str(self.value))


    def message(self, message):
        self.transport.write(message.encode() + b'\n')


from twisted.internet import protocol
from twisted.application import service, internet

factory = protocol.ServerFactory()
factory.protocol = MyChat
factory.clients = []

application = service.Application("chatserver")
internet.TCPServer(1025, factory).setServiceParent(application)



###what to do [steps]###
#Transaction object creation (create n objects for n transactions)
# Block creation by nodes --> hash target implementation - staking hardcoding at this time -- validator will be selected (only 1 validator)
#Block added to blockchain - hashing link (hre implementation - staking hardcoding at this time -- validator will be selected (only 1 validator.tima)
