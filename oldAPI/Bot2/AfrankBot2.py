from DuckwarsApi import *
from Data import *
from SendToNext import *
from RndBot import *
from NextBot import *
from DoNothing import *
from AttackNeutral import *

import time

class AfrankBot2(IBot):
    def __init__(self):
        self.debug=True
        self.data=None
        if self.debug:
            self.log=open('/tmp/bot.log', 'a')
        else:
            self.log=None
        self.round=-1
        
    def logme(self, msg):
        if self.debug:
            self.log.write(msg)
            self.log.flush()

    def doTurn(self, gamestate):
        self.round=self.round+1
        self.logme("start round %d\n"%self.round)
        t1 = time.time()
        # first step, init data
        if self.data==None:
            self.data = Data(gamestate)
        self.data.parse(gamestate)
        self.logme("data parsed\n")
        
        # set alle bots
        bots=[]
        #bots.append(DoNothing(self.data, 0))
        for x in [9,14,19,24,29]: #2,5,10,15,20,30, 50]:
            bots.append(NextBot(self.data, x))
            bots.append(RndBot(self.data, x))
            bots.append(SendToNext(self.data, x))
            bots.append(AttackNeutral(self.data, x))
        self.logme("bots setted\n")
        #self.logme("botslen: %d\n"%(len(bots)))     
        for bot in bots:
            #self.logme(bot.getName()+"\n")
            bot.calc()

        t1a = time.time()
        for bot in bots:
            #print s
            bot.run()
            
        t1b = time.time()
        self.logme("simulat ok,  get best\n")
        for bot in bots:
            s1,s2,s3,r,a,n=bot.get()
            self.logme(str(n)+":   "+ str(s1)+", "+str(s2)+", "+str(s3)+", "+str(a)+"\n")
        bot = self.data.getBest(bots)
        if bot==None:
            self.logme("##################################")
            self.logme("bot was None !!!!!!!!!!!!")
            self.logme("##################################")
            bot=bots[0]
        bot.correction(self.data)
        armies = bot.get()[4]

        self.logme("-----------------------------------------------------------------------\n")
        self.logme("best: "+str(armies)+"\n")
        t2=time.time()  ####################
        
        self.logme("send armies to gamestate\n")
        for a in armies:
            gamestate.issueOrder(gamestate.getCamp(a[A_SRC]), gamestate.getCamp(a[A_DST]), a[A_CNT])
        t3=time.time()
        d1=(t2-t1)*1000
        d2=(t3-t2)*1000
        dall=(t3-t1)*1000
        self.logme(">>>>>  t %d: %d ms %d ms  [%d] ms<<<<<<\n"%(self.round, int(d1), int(d2), int(dall)))
        
    def getName(self):
        return "AfrankBot2"


if __name__ == "__main__":
    myBot = AfrankBot2()
    Helper.executeBot(myBot)
