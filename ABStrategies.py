#ABStrategies.py


def strategySmall(gs, dist):
    """ in this strategy we have very low count of teichs """
    mycamps = gs.getMyCamps()
    for c in mycamps:
        cnt = c.getMancount()
        maxcnt = c.getMaxMancount()
        if cnt > (4/5*maxcnt):
            otherCamp =dist.getClosestOtherCamp(gs, c.getID())
            gs.issueOrder(c, otherCamp, cnt)


#    def sendNextAttack(self, myCamp):
#        enemyCamp = self.dist.getClosestOtherCamp(self.gamestate, myCamp.getID())
#        if(n!=None):
#            mc = myCamp.getMancount()
#            send = (mc*4)/5
#            self.gamestate.issueOrder(fromCamp, toCamp, send)
