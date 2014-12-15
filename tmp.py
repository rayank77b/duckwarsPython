
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
       
               for c in mycamps:
            if self.isCampAttacked(c):
                self.P1_CampGetAttacked(c)
            elif self.isCampFull(c):
                if self.needSomeOneHelp(c):
                    self.P2_sendHelp(c):
                elif self.upgradable(c):
                    self.P3_upgrade(c)
                else:
                    self.sendNextAttack(c, camps)
            else:
                if self.upgradeable(c):
                    self.P3_upgrade(c)


def sendHalfMenIfFull(gs, fromCamp, toCamp):
    if(fromCamp.getMancount()>(fromCamp.getMaxMancount()-2)):
        sendMen = fromCamp.getMancount()/2
        gs.issueOrder(fromCamp, toCamp, sendMen)



if(self.firstTurn):
            # berechne alles, was statisch ist, bzw welche map, welche strategie
            allcamps=gamestate.getCamps()
            self.dist = Distances(allcamps)
            self.firstTurn=False
        else:
            #t1 = time.time()
            myCamps = gamestate.getMyCamps()
            allCamps = gamestate.getCamps()
            notMyCamps = gamestate.getNotMyCamps()
            for c in myCamps:
                n = self.dist.getNextOtherCamp(gamestate, c.getID())
                if(n!=None):
                    sendHalfMenIfFull(gamestate, c, n)
                #else:
                #    n = getNearestCamp(c, myCamps)
                #    if(n!=None):
                #        sendHalfMenIfFull(gamestate, c, n)
            #t2 = time.time()
            #d = (t2-t1)*1000000
            #print "doTurn() %d us"%d






















