import random

import CalcArmy
from Data import *

class RndBot(CalcArmy.CalcArmy):
    def __init__(self, data, max):
        self.data=data
        self.camps=data.camps
        self.max=max
    
    def calc(self):
        campslen=len(self.camps)
        armies=[]
        for i, c in enumerate(self.camps):
            if c[C_OWNER]==1:
                cnt = c[C_CNT]
                src=i
                while cnt>self.max:
                    dst=random.randint(0,campslen-1)
                    if(dst==src):
                        pass
                    cnt=cnt-self.max
                    a=self.data.sendArmy(src, dst, self.max)
                    armies.append(a)
        self.data.sendAll(armies)

    def getName(self):
        return "Rnd Bot %d"%self.max
