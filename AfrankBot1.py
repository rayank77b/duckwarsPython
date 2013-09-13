from DuckwarsApi import *

import math
import time


distances=None

def calculateDistance(source, destination):
    dx = source.getX() - destination.getX()
    dy = source.getY() - destination.getY()
    return int(dx * dx + dy * dy)

def calculateDistances(camps):
    """calculate for all camps an array [][], ditances.
        the matrix has then the distances beetwen the camps"""
    size=len(camps)
    global distances
    distances= [[9999999 for col in range(size)] for row in range(size)]
    for x in range(size):
        for y in range(size):
            if(x!=y):
                distances[x][y]=calculateDistance(camps[x], camps[y])

def getDistance(myid, campid):
    return distances[myid][campid]

def getMinDistance(id):
    """ return the distance of two camps"""
    return min(distances[id])
    
def getNearestCamp(matrix, id):
    """return the id of the nearest capmp with id"""
    return distances[id].index(min(distances[id]))

def getNextOtherCamp(gs, id):
    """ return the id of the neares camp, which not belong to me"""
    ocs = gs.getNotMyCamps()
    c=None
    dis=9999999
    #print distances
    for o in ocs:
        d = getDistance(id, o.getID())
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
    
    def doTurn(self, gamestate):
        if(self.firstTurn):
            # berechne alles, was statisch ist, bzw welche map, welche strategie
            allcamps=gamestate.getCamps()
            calculateDistances(allcamps)
            self.firstTurn=False
            #print getDistance(3, 1)
        else:
            #t1 = time.time()
            myCamps = gamestate.getMyCamps()
            allCamps = gamestate.getCamps()
            notMyCamps = gamestate.getNotMyCamps()
            for c in myCamps:
                n = getNextOtherCamp(gamestate, c.getID())
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
