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
    def testGameSettingsFromData(self):
        env = "ENV 1000 1 1 7 5 20 40 60 80 100 1 2 3 4 5 10 30 50 70"
        data = env[4:].strip()
        gset = GameSettings.fromDataString(data)
        self.failUnlessEqual(gset.MaxGameLength,1000)
        self.failUnlessEqual(gset.OverfullCampDecreseRate, 1)
        self.failUnlessEqual(gset.MaxCampSize,5)
        self.failUnlessEqual(gset.GrowthRate[4], 5)
        self.failUnlessEqual(gset.MaxManCount[3], 80)
        self.failUnlessEqual(gset.UpgradeCost[3],70)
        self.failUnlessEqual(gset.TravelCost, 1)
        self.failUnlessEqual(gset.TravelCostStartsWithTurn, 7)

def createGameState():
    mC1 = "C 2 2 1 20 3\n"   # id 0
    mC2 = "C 10 10 2 20 2\n" # id 1
    mC3 = "C 11 11 0 10 3\n" # id 2
    mC4 = "C 5 5 2 20 3\n"   # id 3
    mA1 = "A 1 10 0 1 10 5\n"
    mA2 = "A 1 10 0 2 10 5\n"
    message = mC1+mC2+mC3+mC4+mA1+mA2
    settings = GameSettings()
    state = GameState(message, ["A","B","C","D"],settings)
    return state

class GameStateFirstTest(unittest.TestCase):
    def testFirstGameStateCreation(self):
        gs = createGameState()
        self.failUnlessEqual(gs.getTeamNames()[0],"A")
        self.failUnlessEqual(gs.getSettings().MaxManCount[3], 80)
        self.failUnlessEqual(gs.getNumCamps(), 4)
        self.failUnlessEqual(gs.getNumArmies(), 2)

class CampTest(unittest.TestCase):        
    def testCamp(self):
        id=0
        campOwner=1
        campMancount=33
        campSize=5
        posX=5
        posY=7
        gs = createGameState()
        c = Camp(id, campOwner, campMancount, campSize, posX, posY, gs)
        self.failUnlessEqual(c.getID(),id)
        self.failUnlessEqual(c.getMancount(),campMancount)
        self.failUnlessEqual(c.getMaxMancount(),campSize*20)
        oldvalue = c.getMancount()
        c.setMancount(20);
        self.failUnlessEqual(c.getMancount(),20)
        c.setMancount(1000);
        self.failUnlessEqual(c.getMancount(),c.getMaxMancount())  # es sollte nicht mehr als max gesetzt werden!
        c.setMancount(oldvalue);
        self.failUnlessEqual(c.getMancount(),campMancount)
        
        self.failUnlessEqual(2,(1+campMancount/20))
        self.failUnlessEqual(c.getGrowthrate(),(1+campMancount/20))   # FIXME: mehr Test zu diese Funktion
        self.failUnlessEqual(c.getOwner(),campOwner)
        self.failUnlessEqual(c.getSize(),campSize)
        self.failUnlessEqual(c.getX(),posX)
        self.failUnlessEqual(c.getY(),posY)

class GameStateTest(unittest.TestCase):
    def testGameState(self):
        gs = createGameState()
        self.failUnlessEqual(gs.getNumCamps(), 4)
        self.failUnlessEqual(gs.getNumArmies(), 2)
        
        a = gs.getArmy(0)
        self.failUnlessEqual(1,a.getDestination())
        self.failUnlessEqual(10,a.getMancount())
        self.failUnlessEqual(1,a.getOwner())
        self.failUnlessEqual(0,a.getSource())
        self.failUnlessEqual(10,a.getTripDuration())
        self.failUnlessEqual(5,a.getTurnsRemaining())


if __name__ == "__main__": 
    unittest.main()
