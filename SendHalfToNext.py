import CalcArmy
from Data import *

class SendHalfToNext(CalcArmy.CalcArmy):
    def __init__(self, data):
        self.data=data
        self.camps=data.camps
    
    def calc(self):
        campslen=len(self.camps)
        armies=[]
        for i, c in enumerate(self.camps):
            if c[C_OWNER]==1:
                cnt = c[C_CNT]/2
                src=i
                if i>=campslen:
                    dst=0
                else:
                    dst=i+1
                a=self.data.sendArmy(src, dst, cnt)
                armies.append(a)
        self.data.sendAll(armies)
                
