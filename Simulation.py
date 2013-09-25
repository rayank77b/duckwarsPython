import copy

from Data import *

def _army_on_dst(a):
    if a[A_REM]>0:  # if 0 then handled,  what happen if we send army to myself?
        a[A_REM]=a[A_REM]-1
        if a[A_REM]==0:  # army is on dest
            return True
    return False

class Simulation:
    def __init__(self, data, send):
        self.camps=copy.deepcopy(data.camps)
        self.send=send # array of armies
        self.rnd5=-999
        self.rnd10=-999
        self.rnd20=-999
        self.rnd50=-999
    
    def get(self):
        return self.rnd5, self.rnd10, self.rnd20, self.rnd50

    def simulate_rate(self):
        '''simulate growth rate'''
        for i, c in enumerate(self.camps):
            if c[C_OWNER]>0:
                if c[C_CNT] > c[C_SIZE]*20:
                    self.camps[i][C_CNT]=c[C_CNT]-1
                elif c[C_CNT] < c[C_SIZE]*20:
                    self.camps[i][C_CNT]=1+c[C_CNT]/20

    def simulate_my_send(self):
        '''simulate sended armies from me'''
        for a in self.send:
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
        ''' run the simulation ''' 
        for round in range(5):
            self.simulate_rate()
            self.simulate_my_send()
        # calculate the sum of my mancount
        sum=0
        for c in self.camps:
            if c[C_OWNER]==1:
                sum = sum + c[C_CNT]
        self.rnd5=sum
        for round in range(5):
            self.simulate_rate()
            self.simulate_my_send()
        # calculate the sum of my mancount
        sum=0
        for c in self.camps:
            if c[C_OWNER]==1:
                sum = sum + c[C_CNT]
        self.rnd10=sum
        for round in range(10):
            self.simulate_rate()
            self.simulate_my_send()
        # calculate the sum of my mancount
        sum=0
        for c in self.camps:
            if c[C_OWNER]==1:
                sum = sum + c[C_CNT]
        self.rnd20=sum
        for round in range(30):
            self.simulate_rate()
            self.simulate_my_send()
        # calculate the sum of my mancount
        sum=0
        for c in self.camps:
            if c[C_OWNER]==1:
                sum = sum + c[C_CNT]
        self.rnd50=sum
                
        
