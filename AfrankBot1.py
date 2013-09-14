from DuckwarsApi import *

import math
import time

from Distances import *



def sendHalfMenIfFull(gs, fromCamp, toCamp):
    if(fromCamp.getMancount()>(fromCamp.getMaxMancount()-2)):
        sendMen = fromCamp.getMancount()/2
        gs.issueOrder(fromCamp, toCamp, sendMen)

class AfrankBot1(IBot):

    def __init__(self):
        self.firstTurn=True
        self.dist=None
    
    def doTurn(self, gamestate):
        if(self.firstTurn):
            # berechne alles, was statisch ist, bzw welche map, welche strategie
            allcamps=gamestate.getCamps()
            self.dist = Distances(allcamps)
            self.firstTurn=False
        else:
            #t1 = time.time()
            myCamps = gamestate.getMyCamps()
            allCamps = gamestate.getCamps()
            notMyCamps = gamestate.getNotMyCamps()
            for c in myCamps:
                n = self.dist.getNextOtherCamp(gamestate, c.getID())
                if(n!=None):
                    sendHalfMenIfFull(gamestate, c, n)
                #else:
                #    n = getNearestCamp(c, myCamps)
                #    if(n!=None):
                #        sendHalfMenIfFull(gamestate, c, n)
            #t2 = time.time()
            #d = (t2-t1)*1000000
            #print "doTurn() %d us"%d
    
    def getName(self):
        return "AfrankBot1"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
