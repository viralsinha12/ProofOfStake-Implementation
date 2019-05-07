"""The most basic chat protocol possible.

run me with twistd -y chatserver.py, and then connect with multiple
telnet clients to port 1025
"""

from __future__ import print_function

from twisted.protocols import basic

class Transaction:

    def __init__(self,transactionId, timeStamp,inputCounter,outputCounter,txid,amount,address1,address2,vouta,voutb,blockTimeStamp,confirmations,signature):
        self.transactionId = transactionId
        # transaction timestamp
        self.timeStamp = timeStamp
        #number of inputs - single/split
        self.inputCounter = inputCounter
        #return value or not
        self.outputCounter = outputCounter
        #Class objects
        self.valueIn = ValueIn(txid, amount,voutb,signature)
        self.valueOut1 = ValueOut(address1,amount, vouta)
        self.valueOut2 = ValueOut(address2, amount, voutb)
        self.blockTimeStamp = blockTimeStamp
        #how many people have confirmed this transactions - ?!?!
        self.confirmations = confirmations


class ValueIn:
    def __init__(self,previousTransactionId,amount,voutIndex,signature):
        self.signature = signature 
        self.previousTransactionId = previousTransactionId
        self.amount = amount
        self.voutIndex = voutIndex

class ValueOut:
    #publickey
    def __init__(self,receiverAddress,amount,outIndex):
        self.receiverAddress = receiverAddress#self public key
        self.amount = amount
        self.outIndex = outIndex

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

# class kernel:
#     #current timestamp when the coin is being staked
#     nTimeTx
#     #(coinstakeTransaction(valueIn->transactionId))-- find this fkn 
#     #particular transaction from #block's listOfTransactions --> get the timestamp for this block
#     nTimeBlockFrom
    

import random
import datetime
import hashlib

global x
x = 0

blockChain = []
unresolvedTransactions = []
transactionList = []
global broadcastValue
broadcastValue = 0
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024,random_generator)
publickey1 = key.publickey()
privatekey1 = key

random_generator = Random.new().read
key = RSA.generate(1024,random_generator)
publickey2 = key.publickey()
privatekey2 = key

random_generator = Random.new().read
key = RSA.generate(1024,random_generator)
publickey3 = key.publickey()
privatekey3 = key

# transactionId, timeStamp,inputCounter,outputCounter,blockTimeStamp,confirmations
now = datetime.datetime.now()
# def __init__(self,transactionId, timeStamp,inputCounter,outputCounter,txid,amount,address1,address2,vouta,voutb,blockTimeStamp,confirmations):
transactionObj1  = Transaction("_xxx101", now, 1, 2, "xxx000", 100, "publickey0", publickey1, 0, 1, None,0,None)
transactionList.append(transactionObj1)

now = datetime.datetime.now()
# def __init__(self,transactionId, timeStamp,inputCounter,outputCounter,txid,amount,address1,address2,vouta,voutb,blockTimeStamp,confirmations):
sig = str(hashlib.sha256(transactionObj1.valueIn.previousTransactionId.encode('utf-8')))+str(publickey2)
sig1 = sig
# sig = hashlib.sha256(sig.encode('utf-8'))
random_generator = Random.new().read
sig = privatekey1.sign(sig.encode('utf-8'),random_generator)
ver = publickey1.verify(sig1.encode('utf-8'),sig)
transactionObj2  = Transaction("_xxx102", now, 1, 2, "_xxx101", 100, publickey1, publickey2, 0, 1, None,0,sig)
transactionList.append(transactionObj2)

now = datetime.datetime.now()
# def __init__(self,transactionId, timeStamp,inputCounter,outputCounter,txid,amount,address1,address2,vouta,voutb,blockTimeStamp,confirmations):
sig = str(hashlib.sha256(transactionObj2.valueIn.previousTransactionId.encode('utf-8')))+str(publickey3)
sig1 = sig
# sig = hashlib.sha256(sig.encode('utf-8'))
random_generator = Random.new().read
sig = privatekey2.sign(sig.encode('utf-8'),random_generator)
ver = publickey2.verify(sig1.encode('utf-8'),sig)
transactionObj3  = Transaction("_xxx103", now, 1, 2, "_xxx102", 100, publickey2, publickey3, 0, 1, None,0,sig)
transactionList.append(transactionObj3)

now = datetime.datetime.now()
transactionObj4  = Transaction("_xxx104", now, 1, 2, "xxx000xxx", 920, "publickey0", publickey1, 0, 1, None,0,None)
transactionList.append(transactionObj4)

now = datetime.datetime.now()
# def __init__(self,transactionId, timeStamp,inputCounter,outputCounter,txid,amount,address1,address2,vouta,voutb,blockTimeStamp,confirmations):
sig = str(hashlib.sha256(transactionObj2.valueIn.previousTransactionId.encode('utf-8')))+str(publickey2)
sig1 = sig
# sig = hashlib.sha256(sig.encode('utf-8'))
random_generator = Random.new().read
sig = privatekey2.sign(sig.encode('utf-8'),random_generator)
ver = publickey2.verify(sig1.encode('utf-8'),sig)
transactionObj5  = Transaction("_xxx105", now, 1, 2, "_xxx104", 920, publickey1, publickey2, 0, 1, None,0,sig)
transactionList.append(transactionObj5)

now = datetime.datetime.now()
# def __init__(self,transactionId, timeStamp,inputCounter,outputCounter,txid,amount,address1,address2,vouta,voutb,blockTimeStamp,confirmations):
sig = str(hashlib.sha256(transactionObj2.valueIn.previousTransactionId.encode('utf-8')))+str(publickey3)
sig1 = sig
# sig = hashlib.sha256(sig.encode('utf-8'))
random_generator = Random.new().read
sig = privatekey2.sign(sig.encode('utf-8'),random_generator)
ver = publickey2.verify(sig1.encode('utf-8'),sig)
transactionObj6  = Transaction("_xxx106", now, 1, 2, "_xxx105", 920, publickey2, publickey3, 0, 1, None,0,sig)
transactionList.append(transactionObj6)

now = datetime.datetime.now()
#copy of TransactionObj2
sig = str(hashlib.sha256(transactionObj2.valueIn.previousTransactionId.encode('utf-8')))+str(publickey3)
sig1 = sig
random_generator = Random.new().read
sig = privatekey1.sign(sig.encode('utf-8'),random_generator)
ver = publickey1.verify(sig1.encode('utf-8'),sig)
transactionObj7  = Transaction("_xxx107", now, 1, 2, "_xxx101", 100, publickey1, publickey3, 0, 1, None,0,sig)
transactionList.append(transactionObj7)

#copy of transaction 5
now = datetime.datetime.now()
# def __init__(self,transactionId, timeStamp,inputCounter,outputCounter,txid,amount,address1,address2,vouta,voutb,blockTimeStamp,confirmations):
sig = str(hashlib.sha256(transactionObj2.valueIn.previousTransactionId.encode('utf-8')))+str(publickey3)
sig1 = sig
# sig = hashlib.sha256(sig.encode('utf-8'))
random_generator = Random.new().read
sig = privatekey2.sign(sig.encode('utf-8'),random_generator)
ver = publickey2.verify(sig1.encode('utf-8'),sig)
transactionObj8  = Transaction("_xxx108", now, 1, 2, "_xxx104", 920, publickey1, publickey3, 0, 1, None,0,sig) 
transactionList.append(transactionObj8)

class POSSystem(basic.LineReceiver):

    def __init(self,value):
        self.value = value

    def connectionMade(self):
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        global x
        global broadcastValue
        self.value = line

        for c in self.factory.clients:
            if c!=self:
                if(line==b'broadcast'):
                    for it in range(0,8):
                        if(it==0):
                            unresolvedTransactions.append(transactionList[it])
                            temp = it + 1
                            c.message("Transaction "+str(temp)+" validated and added to unresolved transactions pool")
                        else:
                            duplicateTransaction = 0
                            status = 1
                            for itr in range(0,it):
                                if(transactionList[it].valueIn.previousTransactionId == transactionList[itr].valueIn.previousTransactionId):
                                    duplicateTransaction = itr + 1    
                                    status = 0

                            if(status==1):
                                unresolvedTransactions.append(transactionList[it])
                                temp = it + 1
                                c.message("Transaction "+str(temp)+" validated and added to unresolved transactions pool")
                            else:
                                c.message("Double Spending detected in transaction : "+str(it+1)+" with transaction  : "+str(duplicateTransaction))        

    def message(self, message):
        self.transport.write(message.encode() + b'\n')


from twisted.internet import protocol
from twisted.application import service, internet
from Crypto.Hash import SHA256
factory = protocol.ServerFactory()
factory.protocol = POSSystem
factory.clients = []
application = service.Application("possystem")
internet.TCPServer(1025, factory).setServiceParent(application)



###what to do [steps]###
#Transaction object creation (create n objects for n transactions)
# Block creation by nodes --> hash target implementation - staking hardcoding at this time -- validator will be selected (only 1 validator)
#Block added to blockchain - hashing link (hre implementation - staking hardcoding at this time -- validator will be selected (only 1 validator at a time)