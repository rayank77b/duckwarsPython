import random

import CalcArmy
from Data import *

class AttackNeutral(CalcArmy.CalcArmy):
    def __init__(self, data):
        self.data=data
        

    def calc(self):
        armies=[]
        
        self.data.sendAll(armies)

    def getName(self):
        return "Attack Neutral Bot "
