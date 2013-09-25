import copy

from Data import *

def _army_on_dst(a):
    if a[A_REM]>0:  # if 0 then handled,  what happen if we send army to myself?
        a[A_REM]=a[A_REM]-1
        if a[A_REM]==0:  # army is on dest
            return True
    return False

def _printC(c, msg):
    print msg, " c ", c[C_X],":",c[C_Y]," ",c[C_OWNER]," ",c[C_CNT]

class Simulation:
    def __init__(self, data, send):
        self.camps=copy.deepcopy(data.camps)
        self.send=send # array of armies
        self.rounds=[]
    
    def get(self):
        return sum(self.rounds), self.rounds, self.send

    def simulate_rate(self):
        '''simulate growth rate'''
        for i, c in enumerate(self.camps):
            if c[C_OWNER]>0:
                #_printC(c, "blub")
                if c[C_CNT] > c[C_SIZE]*20:
                    self.camps[i][C_CNT]=c[C_CNT]-1
                elif c[C_CNT] < c[C_SIZE]*20:
                    self.camps[i][C_CNT]=c[C_CNT]+1+c[C_CNT]/20
                #print "count: ", cnt

    def simulate_my_send(self):
        '''simulate sended armies from me'''
        for a in self.send:
            if _army_on_dst(a):
                #print a
                dst=a[A_DST]
                if a[A_OWNER]==self.camps[dst][C_OWNER]:
                    self.camps[dst][C_CNT]=self.camps[dst][C_CNT] + a[A_CNT]
                else:
                    self.camps[dst][C_CNT]=self.camps[dst][C_CNT] - a[A_CNT]
                if self.camps[dst][C_CNT]<0:
                    self.camps[dst][C_OWNER]=a[A_OWNER]
                    self.camps[dst][C_CNT]= -1*self.camps[dst][C_CNT]

    def simulate_armies(self):
        '''simulate the incoming armies'''
        for i, c in enumerate(self.camps):
            for j, a in enumerate(c[C_ARMY]):
                if _army_on_dst(a):
                    dst=a[A_DST]
                    if a[A_OWNER]==self.camps[dst][C_OWNER]:
                        self.camps[dst][C_CNT]=self.camps[dst][C_CNT] + a[A_CNT]
                    else:
                        self.camps[dst][C_CNT]=self.camps[dst][C_CNT] - a[A_CNT]
                    if self.camps[dst][C_CNT]<0:
                        self.camps[dst][C_OWNER]=a[A_OWNER]
                        self.camps[dst][C_CNT]= -1*self.camps[dst][C_CNT]

    def run(self):
        ''' run the simulation, every 5 round, 5x10= 50 rounds ''' 
        for roundcnt in range(5):
            for round in range(5):
                #_printC(self.camps[9], "vor")
                self.simulate_rate()
                #_printC(self.camps[10], "rate")
                self.simulate_my_send()
                #_printC(self.camps[10], "arm1")
                self.simulate_armies()
                #_printC(self.camps[10], "arm2")
            # calculate the sum of my mancount
            sum=0
            for c in self.camps:
                if c[C_OWNER]==1:
                    sum = sum + c[C_CNT]
            self.rounds.append(sum)

                
        
