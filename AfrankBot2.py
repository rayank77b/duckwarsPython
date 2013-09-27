from DuckwarsApi import *
from Data import *
from SendToNext import *
from RndBot import *
from NextBot import *

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
        # reset the send array
        self.data.send=[]
        
        # set alle bots
        bots=[]
        bots.append(NextBot(self.data, 2))
        #bots.append(NextBot(self.data, 5))
        #bots.append(NextBot(self.data, 10))
        bots.append(NextBot(self.data, 15))
        bots.append(SendToNext(self.data, 2))
        #bots.append(SendToNext(self.data, 5))
        #bots.append(SendToNext(self.data, 10))
        bots.append(SendToNext(self.data, 15))
        bots.append(RndBot(self.data, 2))
        #bots.append(RndBot(self.data, 5))
        #bots.append(RndBot(self.data, 10))
        bots.append(RndBot(self.data, 15))
        self.logme("bots setted\n")
        #self.logme("botslen: %d\n"%(len(bots)))     
        for bot in bots:
            #self.logme(bot.getName()+"\n")
            bot.calc()
        results=[]

        self.logme("sendlen: %d\n"%len(self.data.send))
        t1a = time.time()
        for bot in bots:
            #print s
            bot.run()
            results.append(bot.get())
        t1b = time.time()
        self.logme("simulat ok,  get best\n")
        for r in results:
            self.logme(str(r)+"\n")
        armies = self.data.getBest(results)

        self.logme("-----------------------------------------------------------------------\n")
        self.logme("best: "+str(armies)+"\n")
        t2=time.time()  ####################
        
        self.logme("send armies to gamestate\n")
        for a in armies:
            gamestate.issueOrder(gamestate.getCamp(a[A_SRC]), gamestate.getCamp(a[A_DST]), a[A_CNT])
        t3=time.time()
        d1=(t2-t1)*1000
        d1b=(t1b-t1a)*1000
        d2=(t3-t2)*1000
        self.logme("t %d: %d %d %d \n"%(self.round, int(d1), int(d1b), int(d2)))
        
    def getName(self):
        return "AfrankBot2"


if __name__ == "__main__":
    myBot = AfrankBot2()
    Helper.executeBot(myBot)
