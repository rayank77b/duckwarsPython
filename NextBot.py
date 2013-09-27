import random

import CalcArmy
from Data import *

class NextBot(CalcArmy.CalcArmy):

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
                if cnt> self.max:
                    #print "next: id(",i,") cnt: ", cnt, 
                    src=i
                    dst=self.nextmy(src)
                    #print "  src: ", src, " dst: ", dst
                    if dst>-1 :
                        self.sendArmy(src, dst, cnt)

    def getName(self):
        return "Next Bot %d"%self.max
