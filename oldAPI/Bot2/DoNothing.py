import random

import CalcArmy
from Data import *

class DoNothing(CalcArmy.CalcArmy):
    def calc(self):
        pass
        
    def getName(self):
        return "Do Nothing Bot %d"%self.max
