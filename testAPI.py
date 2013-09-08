#!/usr/bin/env python
#
# simple test of classes and gamestate

import sys
import os

import unittest 

from Army import *
from Camp import *
#from GameState import *

# test Army
class ArmyTest(unittest.TestCase):
    def testArmy(self):
        armyOwner=1
        armySize=20
        armySource=0
        armyDestination=1
        tripLength=5
        remaining=4
        a = Army(armyOwner, armySize, armySource, armyDestination, tripLength, remaining)
        self.failUnlessEqual(a.getDestination(),armyDestination)
        self.failUnlessEqual(a.getOwner(),armyOwner)
        self.failUnlessEqual(a.getSource(),armySource)
        self.failUnlessEqual(a.getMancount(),armySize)
        self.failUnlessEqual(a.getTripDuration(),tripLength)
        self.failUnlessEqual(a.getTurnsRemaining(),remaining)

if __name__ == "__main__": 
    unittest.main()
