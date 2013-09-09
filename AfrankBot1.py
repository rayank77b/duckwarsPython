from DuckwarsApi import *

import math
import time

def calculateDistance(source, destination):
    dx = source.getX() - destination.getX();
    dy = source.getY() - destination.getY();
    return int(dx * dx + dy * dy)

def getNearestCamp(mycamp, camps):
    c=None
    distance=9999999
    for o in camps:
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
        for c in myCamps:
            camps = gamestate.getNotMyCamps()
            n = getNearestCamp(c, camps)
            if(n!=None):
                sendHalfMenIfFull(gamestate, c, n)
            else:
                n = getNearestCamp(c, myCamps)
                if(n!=None):
                    sendHalfMenIfFull(gamestate, c, n)
        t2 = time.time()
        d = (t2-t1)*1000000
        print "%d us"%d
    
    def getName(self):
        return "AfrankBot1"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
