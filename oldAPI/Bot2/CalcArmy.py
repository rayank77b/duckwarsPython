from Data import *
import copy
import math

class CalcArmy(object):
    ''' CalcArmy is the init bot, it must be inheritat and expanded with
        calc() and getName().'''
    def __init__(self, data, max):
        # get it own copy of the camps(armies, dists) array
        self.camps=copy.deepcopy(data.camps)
        self.max=max
        self.send=[]
        self.rounds=[]
        self.perRound=1
        self.roundPeriod=20
        self.sum=0
        self.sum_my_army=0
        self.sum_enemy=0
    
    # calc() getName() should be implemented by bots 
    def calc(self):
        raise NotImplementedError( "Should have implemented this" )
    def getName(self):
        raise NotImplementedError( "Should have implemented this" )

    # TODO: army which is yet incoming should be deleted from array
    def _army_on_dst(self, a):
        ''' return true if the army is on it destination'''
        if a[A_REM]>0:  # if 0 then handled,  what happen if we send army to myself?
            a[A_REM]=a[A_REM]-1
            if a[A_REM]==0:  # army is on dest
                return True
        return False

    def _printC(self, msg):
        ''' for debuging output '''
        for c in self.camps:
            print msg, " c ", c[C_X],":",c[C_Y]," ",c[C_OWNER]," ",c[C_CNT], "  army: ", c[C_ARMY]
        print "-"*80

    def calculateDistance(self, srcid, dstid):
        ''' real destanation length '''
        diff = self.camps[srcid][C_DIST][dstid]
        return int(math.ceil(math.sqrt(diff)))

    def sendArmy(self, srcid, dstid, cnt):
        ''' set an army to send in send array'''
        a=[0,0,0,0,0,0]
        a[A_OWNER]=1
        a[A_CNT]=cnt
        a[A_SRC]=srcid; a[A_DST]=dstid
        trip = self.calculateDistance(srcid, dstid)
        a[A_TRIP]=trip
        a[A_REM]=trip
        self.camps[srcid][C_CNT] = self.camps[srcid][C_CNT] - cnt
        if self.camps[srcid][C_CNT]>=0:
            self.send.append(a) 
        else:
            self.camps[srcid][C_CNT] = self.camps[srcid][C_CNT] + cnt

    def get(self):
        return self.sum, self.sum_my_army, self.sum_enemy, self.rounds, self.send, self.getName()
        #return self.sum, self.sum_my_army, self.sum_enemy, self.send, self.getName()

    def nearest2me(self, id):
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
    
    def nearest2meneutral(self, id):
        dst=self.camps[id][C_DIST]
        #print dst
        dist=9999
        d_id=-1
        for i, d in enumerate(dst):
            if self.camps[i][C_OWNER]==0:
                if d<=dist:
                    dist=d
                    d_id=i
        return d_id

    def my_nearest(self, id):
        dst=self.camps[id][C_DIST]
        #print dst
        dist=9999
        d_id=-1
        for i, d in enumerate(dst):
            if self.camps[i][C_OWNER]==1:
                if d<=dist:
                    dist=d
                    d_id=i
        return d_id

    def _sended_army(self, cid):
        ''' test if we have send some army from a camp with id cid'''
        for army in self.send:
            if cid==army[A_SRC]:
                return True
        return False
    
    def correction(self, data):
        ''' correction look for full camps, which don't send armies and send
            them to the next own camp '''
        camps=data.camps
        for i, c in enumerate(camps):
            if c[C_OWNER]==1:
                if c[C_CNT]>=c[C_SIZE]*20:
                    if not self._sended_army(i):
                        dst=self.my_nearest(i)
                        if (dst>0) and (dst!=i):
                            self.sendArmy(i, dst, int(c[C_CNT]*0.8))

    def _getsum(self, r, i):
        s=0
        for x in r:
            s=s+x[i]
        return s

    def _simulate_rate(self):
        '''simulate growth rate'''
        for i, c in enumerate(self.camps):
            if c[C_OWNER]>0:
                #_printC(c, "blub")
                if c[C_CNT] > c[C_SIZE]*20:
                    self.camps[i][C_CNT]=c[C_CNT]-1
                elif c[C_CNT] < c[C_SIZE]*20:
                    self.camps[i][C_CNT]=c[C_CNT]+1+c[C_CNT]/20
                #print "count: ", cnt

    def _simulate_my_send(self):
        '''simulate sended armies from me'''
        #print "+"*80
        #print self.send
        for a in self.send:
            if self._army_on_dst(a):
                #print a
                dst=a[A_DST]
                if a[A_OWNER]==self.camps[dst][C_OWNER]:
                    #print "own army on camp", a, self.camps[dst][0:5],
                    self.camps[dst][C_CNT]=self.camps[dst][C_CNT] + a[A_CNT]
                    #print "  -> ", self.camps[dst][0:5]
                else:
                    #print "enemy army on camp", a, self.camps[dst][0:5],
                    self.camps[dst][C_CNT]=self.camps[dst][C_CNT] - a[A_CNT]
                    #print "  -> ", self.camps[dst][0:5]
                if self.camps[dst][C_CNT]<0:
                    #print "camps chan: ", self.camps[dst][0:5],
                    self.camps[dst][C_OWNER]=a[A_OWNER]
                    self.camps[dst][C_CNT]= -1*self.camps[dst][C_CNT]
                    #print "  camps changed", self.camps[dst][0:5]

    def _simulate_armies(self):
        '''simulate the incoming armies'''
        #print "-"*80
        for i, c in enumerate(self.camps):
            for j, a in enumerate(c[C_ARMY]):
                if self._army_on_dst(a):
                    dst=a[A_DST]
                    if a[A_OWNER]==self.camps[dst][C_OWNER]:
                        #print "own army on camp", a, self.camps[dst][0:5],
                        self.camps[dst][C_CNT]=self.camps[dst][C_CNT] + a[A_CNT]
                        #print "  -> ", self.camps[dst][0:5]
                    else:
                        #print "enemy army on camp", a, self.camps[dst][0:5],
                        self.camps[dst][C_CNT]=self.camps[dst][C_CNT] - a[A_CNT]
                        #print "  -> ", self.camps[dst][0:5]
                    if self.camps[dst][C_CNT]<0:
                        #print "camps chan: ", self.camps[dst][0:5],
                        self.camps[dst][C_OWNER]=a[A_OWNER]
                        self.camps[dst][C_CNT]= -1*self.camps[dst][C_CNT]
                        #print "  camps changed", self.camps[dst][0:5]

    def run(self):
        ''' run the simulation ''' 
        weight=1.6
        for roundcnt in range(self.roundPeriod):
            for round in range(self.perRound):
                #self._printC("vor1")
                self._simulate_rate()
                #self._printC("rate")
                self._simulate_my_send()
                #self._printC("arm1")
                self._simulate_armies()
                #self._printC("arm2")
                #print "+"*80
            # calculate the sum of my mancount
            sume=0
            sume_my_army=0
            sum_enemy=0
            
            for c in self.camps:
                if c[C_OWNER]==1:
                    cnt = c[C_CNT]
                    # dont sum if the the count max
                    if cnt<(c[C_SIZE]*20):
                        sume = sume + c[C_CNT]   # TODO: should we calculate armies on the way too?
                elif c[C_OWNER]>1:
                    cnt = c[C_CNT]
                    sum_enemy = sum_enemy + c[C_CNT]   # TODO: should we calculate armies on the way too?
            #print "###########   sum: ", sum, weight, int(sum*weight)
            #print "+"*80
            #self.rounds.append(int(sum*weight))
            self.rounds.append((sume,sume_my_army,sum_enemy))
            weight=weight-0.1
        self.sum=self._getsum(self.rounds, 0)
        self.sum_my_army=self._getsum(self.rounds,1)
        self.sum_enemy=self._getsum(self.rounds,2)
