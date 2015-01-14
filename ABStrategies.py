#ABStrategies.py

import random

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

def sendIfWeHaveAbout250Mens(gs,c,cnt):
    if cnt >= 250:
        hostile = gs.getHostileCamps()
        for h in hostile:
            gs.issueOrder(c, h, cnt)
            return True
    return False


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
        elif cnt > maxcnt:
            #bot.logme("get cnt max")
            sendMen = cnt * 0.95
            otherCamp =dist.getClosestOtherCamp(gs, c.getID())
            if otherCamp != None:
                #bot.logme("found other camp")
                maxOther = otherCamp.getMaxMancount()
                if ( sendMen > maxOther ):
                    sendMen = maxOther + 5
                cntOther = otherCamp.getMancount()
                #bot.logme("cntOther: %d,  cnt: %d"%(cntOther,cnt))
                if cntOther+5 > cnt: # i will lost, thus send some men to other my camp
                    #bot.logme("we lost")
                    upgradeCampIfPossible(gs,c, cnt)
                else:
                    gs.issueOrder(c, otherCamp, sendMen)


#    def sendNextAttack(self, myCamp):
#        enemyCamp = self.dist.getClosestOtherCamp(self.gamestate, myCamp.getID())
#        if(n!=None):
#            mc = myCamp.getMancount()
#            send = (mc*4)/5
#            self.gamestate.issueOrder(fromCamp, toCamp, send)
