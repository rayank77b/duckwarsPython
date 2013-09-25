import random

import CalcArmy
from Data import *

class NextBot(CalcArmy.CalcArmy):
    def __init__(self, data):
        self.data=data
        self.camps=data.camps
    
    def nextmy(self, id):
        dst=self.camps[id][C_DIST]
        dist=9999
        d_id=-1
        for i, d in enumerate(dst):
            if self.camps[i][C_OWNER]!=1:
                if dist <= d:
                    dist=d
                    d_id=i
        return d_id
    
    def calc(self):
        campslen=len(self.camps)
        armies=[]
        for i, c in enumerate(self.camps):
            if c[C_OWNER]==1:
                cnt = c[C_CNT]/2
                src=i
                dst=self.nextmy(src)
                if dst>-1 :
                    a=self.data.sendArmy(src, dst, cnt)
                    armies.append(a)
        self.data.sendAll(armies)

    def getName(self):
        return "Next Bot "
