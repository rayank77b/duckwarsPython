#!/usr/bin/env python
#
# simple test of classes and gamestate

import sys
import os

import unittest 

from DuckwarsApi import *

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

class GameSettingsTest(unittest.TestCase):
    def testGameSettingsConstructor(self):
        gset = GameSettings()
        self.failUnlessEqual(gset.MaxCampSize,5)
        self.failUnlessEqual(gset.GrowthRate[4], 5)
        self.failUnlessEqual(gset.MaxManCount[3], 80)
        self.failUnlessEqual(gset.UpgradeCost[3],70)
        self.failUnlessEqual(gset.TravelCost, 1)
        self.failUnlessEqual(gset.TravelCostStartsWithTurn, 7)
        self.failUnlessEqual(gset.OverfullCampDecreseRate, 1)
        self.failUnlessEqual(gset.MaxGameLength,0)
    

if __name__ == "__main__": 
    unittest.main()
