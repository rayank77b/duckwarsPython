
from Strategie import *

class SendNext(Strategie):
    
    def calculate(self):
        myCamps = self.gs.getMyCamps()
        allCamps = self.gs.getCamps()
        notMyCamps = self.gs.getNotMyCamps()
        for c in self.getMyFullCamps():
            n = self.dist.getNextOtherCamp(self.gs, c.getID())
            if(n!=None):
                sendMen = c.getMancount()/2
                self.gs.issueOrder(c, n, sendMen)
