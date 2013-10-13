
from Strategie import *

class AttackEnemy(Strategie):
    
    def calculate(self):
        ret=False
        myCamps = self.gs.getMyCamps()
        for c in myCamps:
            e=self.getNextEnemy(c)
            if(e!=None):
                self.gs.issueOrder(c, e, c.getMancount())
                ret=True
        return ret
