from DuckwarsApi import *

import math
import time
from Distances import *
from SendNext import *

class AfrankBot1(IBot):
    def __init__(self):
        self.firstTurn=True
        self.dist=None
        self.debug=True
        if self.debug:
            self.log=open('/tmp/bot.log', 'a')
        else:
            self.log=None
        
    def logme(self, msg):
        if self.debug:
            self.log.write(msg)
            self.log.flush()
    
    def doTurn(self, gamestate):
        t1 = time.time()
        if(self.firstTurn):
            # berechne alles, was statisch ist, bzw welche map, welche strategie
            allcamps=gamestate.getCamps()
            self.dist = Distances(allcamps)
            self.firstTurn=False
        
        bot=SendNext(gamestate, self.dist)
        bot.calculate()
        t3=time.time()
        dall=(t3-t1)*1000
        self.logme(">>>>>   %d ms <<<<<<\n"%(int(dall)))
    
    def getName(self):
        return "AfrankBot1"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
