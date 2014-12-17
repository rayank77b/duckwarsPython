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
        self.DEBUG = True
        if self.DEBUG == True:
            self.f = open("/tmp/afrankbotlog.txt", 'a')
    
    def doTurn(self, gamestate):
        self.gamestate = gamestate
        if(self.firstTurn):
        # berechne alles, was statisch ist, bzw welche map, welche strategie
            #start = time.time()
            allcamps=gamestate.getCamps()
            self.distances = Distances(allcamps)
            self.firstTurn=False
            self.start()
            #end = time.time()
            #self.logme("start first turn: time: %d"%(end-start))
        else:
            self.start()
        
    def start(self):
        """ the main game routine """
        start = time.time()
        camps = self.gamestate.getCamps()
        mycamps = self.gamestate.getMyCamps()
        mcs = []
        
        # sammeln alle daten 
        for c in mycamps:
            x = myCamp(c.getID(), c.getMancount(), c.getMaxMancount(), c.getCanBeUpgraded(), c.getGrowthrate())
            mcs.append(x)
        # sammeln aller angriffe/hilfen
        armies = getAllArmy(self.gamestate)
        for mc in mcs:
            mc.appendArmy(armies)
        
        # generate attack muster
        # 1. Attack: do nothing
        attack = generateAttack(mcs, self.distances, self.gamestate, 10000000)
        attacks.append(attack)

        # 2. Attack: send half to the next, if full
        attack = generateAttack(mcs, camps, self.distances, self.gamestate, 2)
        attacks.append(attack)

        # 3.  Attack: send all men  to the next, if full
        attack = generateAttack(mcs, camps, self.distances, self.gamestate, 1)
        attacks.append(attack)

        self.logAttacks(attacks)

        # simulation
        simulate(attacks, camps)
        
        # choose the best
        # at time we send simple the second attack
        attack = attacks[2]
        
        # generate issueOrder
        for cmps in attack:
            for x in range(1,len(cmps)):
                if cmps[x] != 0:
                    self.gamestate.issueOrder(camps[cmps[0]], camps[x], cmps[x])
        
        end = time.time()
        self.logme("time for start(): %d"%(end-start))
                    
    def logme(self, message):
        if self.DEBUG == True:
            self.f.write(message+"\n")
            self.f.flush()

    def logAttacks(self, attacks):
        if self.DEBUG == True:
            self.f.write("attacks:\n")
            for attack in attacks:
                self.f.write("   attack:\n")
                for camps in attack:
                    self.f.write("     camp: ")
                    for c in camps:
                        self.f.write("%d "%c)
                    self.f.write("\n")
            self.f.flush()

    def getName(self):
        return "AfrankBotV03|PythonTeam"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
