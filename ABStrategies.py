#ABStrategies.py

import random
import math

def getAllArmies(gs):
    cnt = gs.getNumArmies()
    armies = []
    for x in range(cnt):
        armies.append(gs.getArmy(x))
    return armies

def isCampAttacked(gs, c):
    """get information about attack to Camp c"""
    cnt = gs.getNumArmies()
    dest = c.getID()
    for x in range(cnt):
        a = gs.getArmy(x)
        if a.getOwner() != 1:  # meine Armee ist Zero ID
            if a.getDestination() == dest:
                return True
    return False

def upgradeSmallIfSmaller(gs,c,cnt, size):
    if c.getSize() <= size:
        return upgradeCampIfPossible(gs,c, cnt)
    return False
    
def upgradeCampIfPossible(gs,c, cnt):
    if c.getCanBeUpgraded():
        if c.getUpgradeCost() <= cnt:
            gs.upgradeCamp(c)
            return True
    return False
    
def sendHelp(gs, dist, c, cnt, maxcnt, p=0.5):
    myNextCamp = dist.getClosestMyCamp(gs, c.getID())
    if myNextCamp != None:
        if(cnt > maxcnt*0.8):
            if random.randint(0, 1) == 1:
                if gs.calculateTravelCost(c,myNextCamp) < 10:
                    gs.issueOrder(c, myNextCamp, cnt*0.5)
                    return True
    return False

def foundNextWeakAndAttack(gs,dist,c,cnt):
    hostile = gs.getNotMyCamps()
    for h in hostile:
        d = gs.calculateDistance(c,h)
        if d < 7:  # keine lange distances laufen
            hostileCount = h.getMancount()
            if cnt > hostileCount*3:
                gs.issueOrder(c, h, cnt/2)
                return True
    return False

def willWeWin(gs, c, h, cnt):
    hostileCount = h.getMancount()
    travelCost = gs.calculateTravelCost(c,h)
    rate = h.getGrowthrate()
    rounds = gs.calculateDistance(c,h)
    if cnt > ( hostileCount+travelCost +2 +rate*rounds ):
        return True
    return False

def foundAllWeakAndAttackNext(gs,dist,c,cnt):
    hostile = gs.getNotMyCamps()
    if isCampAttacked(gs, c):
        return False
    for h in hostile:
        if willWeWin(gs,c,h,cnt):
            gs.issueOrder(c, h, cnt)
            return True
    return False

def sendIfWeHaveAbout250Mens(gs,c,cnt):
    if cnt >= 250:
        hostile = gs.getHostileCamps()
        for h in hostile:
            gs.issueOrder(c, h, cnt)
            return True
    return False

def cntGreatMax(gs, dist, c, cnt, maxcnt):
    if cnt > maxcnt:
        sendMen = cnt * 0.95
        otherCamp =dist.getClosestOtherCamp(gs, c.getID())
        if otherCamp != None:
            maxOther = otherCamp.getMaxMancount()
            if ( sendMen > maxOther ):
                sendMen = maxOther + 5
            cntOther = otherCamp.getMancount()
            if cntOther+5 > cnt: # i will lost, thus send some men to other my camp
                return upgradeCampIfPossible(gs,c, cnt)
            else:
                gs.issueOrder(c, otherCamp, sendMen)
                return True
    return False

def sendIfMaxToOneWhichWeCanWin(gs,dist,  c,cnt, maxcnt):
    # if i get attacked, i should wait
    if isCampAttacked(gs, c):
        return False
    if cnt>=maxcnt :
        otherCamp =dist.getClosestOtherCamp(gs, c.getID())
        if otherCamp != None:
            gs.issueOrder(c, otherCamp, cnt)
            return True
    if cnt>=maxcnt :
        hostile = gs.getNotMyCamps()
        for h in hostile:
            hcnt = h.getMancount()
            travel = gs.calculateTravelCost(c,h)
            if cnt > (hcnt+travel):
                gs.issueOrder(c, h, cnt)
                return True
    return False
    
def simpleSendOneMan(gs, c, cnt, mx, bot):
    if isCampAttacked(gs, c):
        return False
    myCamps=gs.getMyCamps()
    camps = gs.getNotMyCamps()
    #bot.logme("we are in simpleSendOneMan")
    if len(myCamps)>1:   # wir haben mehr als ein Camp, dann ist es nicht notwendig
        return False
    if cnt == (mx+2):   # wir haben voll und nur ein Camp
        nr=random.randint(0,len(camps)-1)
        gs.issueOrder(c, camps[nr], 20)
    return False

#############################################################################

def strategyFull(gs, dist, bot):
    """ in this strategy we have very low count of teichs """
    mycamps = gs.getMyCamps()
    #bot.logme("strategyFull")
    for c in mycamps:
        cnt = c.getMancount()
        maxcnt = c.getMaxMancount() - 2
        if sendIfWeHaveAbout250Mens(gs,c,cnt):
            pass
        # irgendwo schon meine eigene in der naehe ist sende lieber dorthin, mit 50% wahrscheinlichkeit
        elif sendHelp(gs,dist,c,cnt,maxcnt):
            pass
        # ist jemmand in der naehe den wir ueberrennen koennen?
        elif foundAllWeakAndAttackNext(gs,dist,c,cnt):
            pass
        # falls genug soldaten da sind
        elif cntGreatMax(gs, dist, c, cnt, maxcnt):
            pass
        elif simpleSendOneMan(gs, c, cnt, maxcnt, bot):
            pass

def strategySmall(gs, dist, bot):
    """ in this strategy we have very low count of teichs """
    mycamps = gs.getMyCamps()
    for c in mycamps:
        cnt = c.getMancount()
        maxcnt = c.getMaxMancount() - 2
        if sendIfWeHaveAbout250Mens(gs,c,cnt):
            pass
        elif upgradeSmallIfSmaller(gs,c,cnt,2):
            pass
        # irgendwo schon meine eigene in der naehe ist sende lieber dorthin, mit 50% wahrscheinlichkeit
        elif sendHelp(gs,dist,c,cnt,maxcnt):
            pass
        # ist jemmand in der naehe den wir ueberrennen koennen?
        elif foundNextWeakAndAttack(gs,dist,c,cnt):
            pass
        # falls genug soldaten da sind
        elif cntGreatMax(gs, dist, c, cnt, maxcnt):
            pass


#    def sendNextAttack(self, myCamp):
#        enemyCamp = self.dist.getClosestOtherCamp(self.gamestate, myCamp.getID())
#        if(n!=None):
#            mc = myCamp.getMancount()
#            send = (mc*4)/5
#            self.gamestate.issueOrder(fromCamp, toCamp, send)
