
from Strategie import *

class FirstSend(Strategie):
    
    def calculate(self):
        ret=False
        myCamps = self.gs.getMyCamps()
        for c in myCamps:
            myCount=c.getMancount()
            for n in self.getNearestNeutralCamps(c, radius=5):
                ncnt=n.getMancount()
                if myCount>ncnt:
                    self.gs.issueOrder(c, n, ncnt+2)
                    myCount=myCount-(ncnt+2)
                    ret=True
        return ret
                
