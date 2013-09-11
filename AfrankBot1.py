from DuckwarsApi import *

import math
import time

def calculateDistance(source, destination):
    dx = source.getX() - destination.getX()
    dy = source.getY() - destination.getY()
    return int(dx * dx + dy * dy)

def calculateDistances(camps):
    """calculate for all camps an array [][], ditances.
        the matrix has then the distances beetwen the camps"""
    size=len(camps)
    r= [[9999999 for col in range(size)] for row in range(size)]
    for x in range(size):
        for y in range(size):
            if(x!=y):
                r[x][y]=calculateDistance(camps[x], camps[y])
    return r

def getMinDistance(matrix, id):
    """ return the distance of two camps"""
    return min(matrix[id])
    
def getNearestCamp(matrix, id):
    """return the id of the nearest capmp with id"""
    return matrix[id].index(min(matrix[id]))

def getNearesOtherCamp(mycamp, camps):
    """ return the id of the neares camp, which not belong to me"""
    c=None
    distance=9999999
    for o in camps:
        d=calculateDistance(mycamp, o)
        if((d<distance)and (d>0)):
            c=o
            distance=d
    return c     

def sendHalfMenIfFull(st, fromCamp, toCamp):
    if(fromCamp.getMancount()>(fromCamp.getMaxMancount()-2)):
        sendMen = fromCamp.getMancount()/2
        st.issueOrder(fromCamp, toCamp, sendMen)

class AfrankBot1(IBot):
    def doTurn(self, gamestate):
        t1 = time.time()
        myCamps = gamestate.getMyCamps()
        allCamps = gamestate.getCamps()
        notMyCamps = gamestate.getNotMyCamps()
        distances=calculateDistances(allCamps)
        for c in myCamps:
            n = getNearesOtherCamp(c, notMyCamps)
            if(n!=None):
                sendHalfMenIfFull(gamestate, c, n)
            #else:
            #    n = getNearestCamp(c, myCamps)
            #    if(n!=None):
            #        sendHalfMenIfFull(gamestate, c, n)
        t2 = time.time()
        d = (t2-t1)*1000000
        print "doTurn() %d us"%d
    
    def getName(self):
        return "AfrankBot1"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
