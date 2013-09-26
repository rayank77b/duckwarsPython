import random

import CalcArmy
from Data import *

class DoNothing(CalcArmy.CalcArmy):
    def __init__(self, data):
        self.data=data
        self.camps=data.camps

    def calc(self):
        armies=[]
        
        self.data.sendAll(armies)

    def getName(self):
        return "Do Nothing Bot "
