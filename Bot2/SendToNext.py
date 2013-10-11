import CalcArmy
from Data import *

class SendToNext(CalcArmy.CalcArmy):
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
                    self.sendArmy(src, dst, cnt)
    
    def getName(self):
        return "SendTNxt %d"%self.max
