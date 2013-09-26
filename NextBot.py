import random

import CalcArmy
from Data import *

class NextBot(CalcArmy.CalcArmy):
    def __init__(self, data):
        self.data=data
        self.camps=data.camps
    
    def nextmy(self, id):
        dst=self.camps[id][C_DIST]
        #print dst
        dist=9999
        d_id=-1
        for i, d in enumerate(dst):
            if self.camps[i][C_OWNER]!=1:
                if d<=dist:
                    dist=d
                    d_id=i
        return d_id
    
    def calc(self):
        campslen=len(self.camps)
        armies=[]
        #print "next: ",campslen
        for i, c in enumerate(self.camps):
            #print c[0:4]
            if c[C_OWNER]==1:
                cnt = c[C_CNT]/2
                #print "next: id(",i,") cnt: ", cnt, 
                src=i
                dst=self.nextmy(src)
                #print "  src: ", src, " dst: ", dst
                if dst>-1 :
                    a=self.data.sendArmy(src, dst, cnt)
                    armies.append(a)
        self.data.sendAll(armies)

    def getName(self):
        return "Next Bot "
