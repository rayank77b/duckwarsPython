#ABStrategies.py


def strategySmall(gs, dist, bot):
    """ in this strategy we have very low count of teichs """
    mycamps = gs.getMyCamps()
    for c in mycamps:
        cnt = c.getMancount()
        maxcnt = c.getMaxMancount() - 2
        if cnt > maxcnt:
            sendMen = cnt * 0.8
            otherCamp =dist.getClosestOtherCamp(gs, c.getID())
            if otherCamp != None:
                maxOther = otherCamp.getMaxMancount()
                if ( sendMen > maxOther ):
                    sendMen = maxOther + 2
                cntOther = otherCamp.getMancount()
                if cntOther > cnt: # i will lost, thus send some men to other my camp
                gs.issueOrder(c, otherCamp, sendMen)


#    def sendNextAttack(self, myCamp):
#        enemyCamp = self.dist.getClosestOtherCamp(self.gamestate, myCamp.getID())
#        if(n!=None):
#            mc = myCamp.getMancount()
#            send = (mc*4)/5
#            self.gamestate.issueOrder(fromCamp, toCamp, send)