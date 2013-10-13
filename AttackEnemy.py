
from Strategie import *

class AttackEnemy(Strategie):
    
    def calculate(self):
        ret=False
        for c in self.getMyFullCamps():
            n = self.dist.getNextOtherCamp(self.gs, c.getID())
            if(n!=None):
                sendMen = c.getMancount()/2
                self.gs.issueOrder(c, n, sendMen)
                ret=True
        return ret
