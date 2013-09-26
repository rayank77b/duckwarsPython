import CalcArmy
from Data import *

class SendHalfToNext(CalcArmy.CalcArmy):
    def __init__(self, data, max):
        self.data=data
        self.camps=data.camps
        self.max = max
    
    def calc(self):
        campslen=len(self.camps)
        armies=[]
        #print "campslen: ", campslen
        for i, c in enumerate(self.camps):
            if c[C_OWNER]==1:
                #print "camp: ",c[0:5]
                #print "army: ",c[5]
                #print "dist: ",c[6]
                cnt = c[C_CNT]/2
                if cnt>=self.max:
                    src=i
                    if i>=(campslen-1):
                        dst=0
                    else:
                        dst=i+1
                    #print "i: ", i, "  src: ", src, "  dst: ", dst, "  cnt: ",cnt
                    a=self.data.sendArmy(src, dst, cnt)
                    armies.append(a)
        self.data.sendAll(armies)
    def getName(self):
        return "SendHalfToNext"
