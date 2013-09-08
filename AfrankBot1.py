from Army import *
from Camp import *
from GameState import *
from Helper import *

import math

def calculateDistance(source, destination):
    dx = source.getX() - destination.getX();
    dy = source.getY() - destination.getY();
    return int(math.ceil(math.sqrt(dx * dx + dy * dy)))
        
def getNearestCamp(mycamp, camps):
    c=None
    distance=9999999
    for o in camps:
        d=calculateDistance(mycamp,o)
        if(d<distance):
            c=o
            distance=d
    return c

class AfrankBot1(IBot):
    def doTurn(self, gamestate):
        myCamps = gamestate.getMyCamps()
        for c in myCamps:
            camps = gamestate.getNotMyCamps()
            n = getNearestCamp(c, camps)
            if(n!=None):
                if(c.getMancount()>(c.getMaxMancount()-2)):
                    sendMen = c.getMancount()/2
                    gamestate.issueOrder(c, n, sendMen)
    
    def getName(self):
        return "AfrankBot1"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
