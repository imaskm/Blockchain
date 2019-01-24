'''
Created on Mar 30, 2018

@author: Dell
'''
import hashlib
from datetime import datetime

class Block():

    def __init__(self,index,data,previous_hash = '',time_stamp = datetime.now() ):
        self.__index            = index
        self.__time_stamp       = time_stamp
        self.__data             = data
        self.__previous_hash    = previous_hash
        self.__hash             = self.calculateHash()

    def get_index(self):
        return self.__index


    def get_time_stamp(self):
        return self.__time_stamp


    def get_data(self):
        return self.__data


    def get_previous_hash(self):
        return self.__previous_hash


    def get_hash(self):
        return self.__hash


    def set_index(self, value):
        self.__index = value


    def set_time_stamp(self, value):
        self.__time_stamp = value


    def set_data(self, value):
        self.__data = value


    def set_previous_hash(self, value):
        self.__previous_hash = value


    def set_hash(self, value):
        self.__hash = value


    def del_index(self):
        del self.__index


    def del_time_stamp(self):
        del self.__time_stamp


    def del_data(self):
        del self.__data


    def del_previous_hash(self):
        del self.__previous_hash


    def del_hash(self):
        del self.__hash
    
    def __str__(self):
        return str( str(self.get_index())+"\n  Data:  "+str(self.get_data())+"\n  Hash :  "+str( self.get_hash() )+"\n Previous Hash:   "+ str( self.get_previous_hash() )+"\n Timestamp  "+str(self.get_time_stamp() ) )
    
        
    
    def calculateHash(self):
        
        hashed = hashlib.sha256( str(str(self.get_index())+ self.get_previous_hash() + str(self.get_time_stamp()) + str(self.get_data()) ).encode('UTF-8') )
        
        digest = hashed.hexdigest()
        
        return str(digest)
    
class BlockChain():
    
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
    
    def createGenesisBlock(self):
        return Block(0,'Genesis Block')
    
    def getLatestBlock(self):
        
        return self.chain[len(self.chain)-1]
    
    def addNewBlock(self,new_block):
        
        new_block.set_previous_hash(self.getLatestBlock().get_hash())
        #Hash is updated as Value of previous Hash is changed
        new_block.set_hash(new_block.calculateHash())
        
        self.chain.append(new_block)
        
    def isChainValid(self):
        
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous= self.chain[i-1]
            
            if(current.get_hash() != current.calculateHash() ):
                return False
            
            if(current.get_previous_hash() != previous.get_hash() ):
                return False
        
        return True

    def printChain(self):

        for block in self.chain:
            print(block)
            
    
chain = BlockChain()

chain.addNewBlock(Block(1,{'data':'Test'}))
chain.addNewBlock(Block(2,{'data1':'Test1'}))

if(chain.isChainValid()):
    chain.printChain()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


    
  