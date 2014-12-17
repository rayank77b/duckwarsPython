# here are some functions
from DuckwarsApi import *

def getAllArmy(gs):
    cnt = gs.getNumArmies()
    armies = []
    for x in range(cnt):
        armies.append(gs.getArmy(x))
    return armies

def getArmiesAttackedCamp(gs, c):
    cnt = gs.getNumArmies()
    dest = c.getID()
    armies = []
    for x in range(cnt):
        a = gs.getArmy(x)
        if a.getOwner() != 0:  # meine Armee ist Zero ID
            if a.getDestination() == dest:
                armies.append(a)
    return armies

def isCampAttacked(gs, c):
    """get information about attack to Camp c"""
    cnt = gs.getNumArmies()
    dest = c.getID()
    for x in range(cnt):
        a = gs.getArmy(x)
        if a.getOwner() != 0:  # meine Armee ist Zero ID
            if a.getDestination() == dest:
                return True
    return False


def summeAfterNRounds(camp_id, rounds, camps):
    

def simulate(attacks, camps, rounds):
    summe=[]
    for attack in attacks:
        camp_summe = 0  
        for cmps in attack:
            camp_id = cmps[0]
            rate = camps[camp_id].getGrowthrate()
            camp_summe = camp_summe + camps[camp_id].getMancount()
            ids=[x for x in cmps if x!=0]  # first number ist the id of the camp
            # zur zeit ohne round trip, armee kommt sofort an
            if len(ids) > 1:
                for i in range(1,len(ids)):
                    cnt_attack = ids[i]
                    camp_summe = camp_summe - cnt_attack
                    
            for x in range(rounds):
            
                
                    



#    def P1_CampGetAttacked(self, c):
#        enemies = self.getArmiesAttackedCamp(c)
#        #at moment we simple wait
#        #minRound = 
#        #manCountAll =
#
#    def isCampFull(self, c):
#        return c.getMancount() == c.getMaxMancount()
#    
#    def needSomeOneHelp(self, c):
#        return False
#        
#    def P2_sendHelp(self,c):
#        pass
#    
#    def upgradable(self, c):
#        return False
#    
#    def P3_upgrade(self, c):
#        return pass
#    
#    def sendNextAttack(self, myCamp):
#        enemyCamp = self.dist.getClosestOtherCamp(self.gamestate, myCamp.getID())
#        if(n!=None):
#            mc = myCamp.getMancount()
#            send = (mc*4)/5
#            self.gamestate.issueOrder(fromCamp, toCamp, send)
