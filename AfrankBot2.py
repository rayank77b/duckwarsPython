from DuckwarsApi import *
from Data import *
from SendHalfToNext import *
from RndBot import *
from Simulation import *
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
        self.round=0
        
    def logme(self, msg):
        if self.debug:
            self.log.write(msg)
            self.log.flush()

    def doTurn(self, gamestate):
        self.round=self.round+1
        t1 = time.time()
        # first step, init data
        if self.data==None:
            self.data = Data(gamestate)
        self.data.parse(gamestate)
        # reset the send array
        self.data.send=[]
        
        # set alle bots
        bots=[]
        bots.append(NextBot(self.data))
        #self.logme("botslen: %d\n"%(len(bots)))     
        for bot in bots:
            bot.calc()
        results=[]
        
        #self.logme("sendlen: %d\n"%len(self.data.send))
        t1a = time.time()
        for s in self.data.send:
            #print s
            sim = Simulation(self.data, s)
            sim.run()
            results.append(sim.get())
        #print results
        t1b = time.time()
        armies = self.data.getBest(results)
        
        t2=time.time()  ####################
        
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
