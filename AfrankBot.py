from DuckwarsApi import *
from Distances import *
from myCamp import *
from myfunc import *

import math
import time

__author__ = "Andrej Frank"
__copyright__ = "Copyright 2014, IT-Designers"
__license__ = "GPL"
__version__ = "3.0.3"
__maintainer__ = "Andrej Frank"
__email__ = "andrej.frank@stz-softwaretechnik.de"
__status__ = "Beta"

class AfrankBot1(IBot):
    def __init__(self):
        self.firstTurn = True
        self.distances = None
        self.gamestate = None
        self.DEBUG = False
        if self.DEBUG == True:
            self.f = open("/tmp/afrankbotlog.txt", 'a')
    
    def doTurn(self, gamestate):
        self.gamestate = gamestate
        if(self.firstTurn):
        # berechne alles, was statisch ist, bzw welche map, welche strategie
            #start = time.time()
            allcamps=gamestate.getCamps()
            self.dist = Distances(allcamps)
            self.firstTurn=False
            self.start()
            #end = time.time()
            #self.logme("start first turn: time: %d"%(end-start))
        else:
            self.start()
        
    def start(self):
        """ the main game routine """
        camps = self.gamestate.getCamps()
        mycamps = self.gamestate.getMyCamps()
        mcs = []
        for c in mycamps:
            x = myCamp(c.getID(), c.getMancount(), c.getMaxMancount(), c.getCanBeUpgraded()):
            mcs.append(x)
            
        armies = getAllArmy(self.gamestate)
        for mc in mcs:
            mc.appendArmy(armies)
            
            
    def logme(self, message):
        if self.DEBUG == True:
            self.f.write(message+"\n")
            self.f.flush()
        
    def getName(self):
        return "AfrankBotV03|PythonTeam"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
