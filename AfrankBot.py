from DuckwarsApi import *

import math
import time

__author__ = "Andrej Frank"
__copyright__ = "Copyright 2014, IT-Designers"
__license__ = "GPL"
__version__ = "3.0.2"
__maintainer__ = "Andrej Frank"
__email__ = "andrej.frank@stz-softwaretechnik.de"
__status__ = "Beta"

class Distances():
    """ build a matrix of all distances between all camps, 
        must be do one time in begin of game (first round)
        after the build ass search are staticaly and very fast"""
    def __init__(self, camps):
        """ calculate for all camps an array [][], ditances.
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

    def getClosest(self, id):
        """ return the closest camp to camp with id. """
        return min(self.distances[id])
    
    def getClosestId(self, id):
        """return the id of the nearest capmp with id"""
        m = min(self.distances[id])
        return self.distances[id].index(m)

    def getClosestOtherCamp(self, gs, id):
        """ return the id of the closest camp, which not belong to me"""
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



class AfrankBot1(IBot):
    def __init__(self):
        self.firstTurn = True
        self.distances = None
        self.gamestate = None
        self.DEBUG = True
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

    def sendMen(self, fromCamp, toCamp):
        mc = fromCamp.getMancount()
        travel_cost = self.gamestate.calculateTravelCost(fromCamp, toCamp)
        upgrade_cost = fromCamp.getUpgradeCost()
        #self.logme("travelcost: %d\nupgradecost: %d\n"%(travel_cost, upgrade_cost))
        
        if( mc > (fromCamp.getMaxMancount()-2)):   # falls voll sende 4/5 
            send = (mc*4)/5
            self.gamestate.issueOrder(fromCamp, toCamp, send)
        elif((toCamp.getMancount()+travel_cost)< (mc-2)):
            self.gamestate.issueOrder(fromCamp, toCamp, (mc-2))
       # elif( fromCamp.getCanBeUpgraded()):
       #     if( fromCamp.getUpgradeCost() > (mc-5) ):
       #         self.gamestate.upgradeCamp(fromCamp)
            

    def start(self):
        """ the main game routine """
        camps = self.gamestate.getCamps()
        mycamps = self.gamestate.getMyCamps()
        for c in mycamps:
            n = self.dist.getClosestOtherCamp(self.gamestate, c.getID())
            if(n!=None):
                self.sendMen(c, n)


    def logme(self, message):
        if self.DEBUG == True:
            self.f.write(message+"\n")
            self.f.flush()
        
    def getName(self):
        return "AfrankBotV02|PythonTeam"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
