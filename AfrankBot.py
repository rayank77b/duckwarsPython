from DuckwarsApi import *

import math
import time

__author__ = "Andrej Frank"
__copyright__ = "Copyright 2014, IT-Designers"
__license__ = "GPL"
__version__ = "2.0.0"
__maintainer__ = "Andrej Frank"
__email__ = "andrej.frank@stz-softwaretechnik.de"
__status__ = "Beta"

class Distances():
    def __init__(self, camps):
        """ Constructor
            calculate for all camps an array [][], ditances.
            the matrix has then the distances beetwen the camps"""
        self.camps_size=len(camps)
        self.distances= [[9999999 for col in range(self.camps_size)] for row in range(self.camps_size)]
        for x in range(self.camps_size):
            for y in range(self.camps_size):
                if(x!=y):
                    self.distances[x][y]=self.calculate(camps[x], camps[y])
                
    def calculate(self, s, d):
        dx = s.getX() - d.getX()
        dy = s.getY() - d.getY()
        return int(dx * dx + dy * dy)

    def out(self):
        for x in range(self.camps_size):
            print self.distances[x]

    def get(self, myid, campid):
        return self.distances[myid][campid]

    def getMin(self, id):
        """ return the distance of two camps"""
        return min(self.distances[id])
    
    def getNearestId(self, id):
        """return the id of the nearest capmp with id"""
        m = min(self.distances[id])
        return self.distances[id].index(m)

    def getNextOtherCamp(self, gs, id):
        """ return the id of the neares camp, which not belong to me"""
        ocs = gs.getNotMyCamps()
        c=None
        dis=9999999
        #print distances
        for o in ocs:
            d = self.get(id, o.getID())
            if d<dis :
                dis=d
                c=o
        return c


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
