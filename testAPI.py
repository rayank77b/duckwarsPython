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

# helper for create a game state
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
    """this is only, because we must first test if GameState is working, 
        because class Camp use it"""
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
        campMancount=60
        campSize=3
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
        self.failUnlessEqual(4,(1+campMancount/20))
        
        self.failUnlessEqual(c.getGrowthrate(), 0) #(1+campMancount/20))   # FIXME: mehr Test zu diese Funktion
        self.failUnlessEqual(c.getMaxGrowthrate(), 3)
        self.failUnlessEqual(c.getCanBeUpgraded(), True) 
        self.failUnlessEqual(c.getUpgradeCost(), 50) 
        
        self.failUnlessEqual(c.getOwner(),campOwner)
        
        self.failUnlessEqual(c.getSize(),campSize)
        c.setSize(5)
        self.failUnlessEqual(c.getSize(),campSize+2)
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
        
        a = gs.getMyArmies()
        self.failUnlessEqual(len(a), 2)
        
        c0 = gs.getCamp(0)
        c1 = gs.getCamp(1)
        c2 = gs.getCamp(2)
        c3 = gs.getCamp(3)
        self.failUnlessEqual(2, c2.getID())
        self.failUnlessEqual(10,c2.getMancount())
        self.failUnlessEqual(60,c2.getMaxMancount())
        self.failUnlessEqual((1+20/20),c1.getGrowthrate())  # fehlerhaft, die rate 
        self.failUnlessEqual(0,c2.getOwner())
        self.failUnlessEqual(3,c2.getSize())
        self.failUnlessEqual(11, c2.getX())
        self.failUnlessEqual(11,c2.getY())
        

        self.failUnlessEqual(gs.calculateTravelCost(c0, c1), 5);
        self.failUnlessEqual(gs.calculateTravelCost(c0, c3), 0);
        
        cs = gs.getCamps()
        self.failUnlessEqual(4, len(cs))
        c2 = cs[2]
        self.failUnlessEqual(2, c2.getID())
        self.failUnlessEqual(10,c2.getMancount())
        self.failUnlessEqual(60,c2.getMaxMancount())
        self.failUnlessEqual(1,c2.getGrowthrate()) 
        self.failUnlessEqual(0,c2.getOwner())
        self.failUnlessEqual(3,c2.getSize())
        self.failUnlessEqual(11, c2.getX())
        self.failUnlessEqual(11,c2.getY())
        
        hostile = gs.getHostileCamps()
        self.failUnlessEqual(2,len(hostile))
        c2 = hostile[0]   #mC2 = "C 10 10 2 20 2\n" # id 1
        self.failUnlessEqual(1, c2.getID())
        self.failUnlessEqual(20,c2.getMancount())
        self.failUnlessEqual(40,c2.getMaxMancount())
        #print c2
        self.failUnlessEqual((1+20/20),c2.getGrowthrate())
        self.failUnlessEqual(2,c2.getOwner())
        self.failUnlessEqual(2,c2.getSize())
        self.failUnlessEqual(10, c2.getX())
        self.failUnlessEqual(10,c2.getY())
        
        myCamps = gs.getMyCamps()
        self.failUnlessEqual(1,len(myCamps))
        c2 = myCamps[0]   #mC1 = "C 2 2 1 20 3\n"   # id 0
        self.failUnlessEqual(0, c2.getID())
        self.failUnlessEqual(20,c2.getMancount())
        self.failUnlessEqual(60,c2.getMaxMancount())
        self.failUnlessEqual((1+20/20),c2.getGrowthrate())
        self.failUnlessEqual(1,c2.getOwner())
        self.failUnlessEqual(3,c2.getSize())
        self.failUnlessEqual(2, c2.getX())
        self.failUnlessEqual(2,c2.getY())
        
        neutralCamps = gs.getNeutralCamps()
        self.failUnlessEqual(1,len(neutralCamps))
        c2 = neutralCamps[0]   #mC3 = "C 11 11 0 10 3\n" # id 2
        self.failUnlessEqual(2, c2.getID())
        self.failUnlessEqual(10,c2.getMancount())
        self.failUnlessEqual(60,c2.getMaxMancount())
        self.failUnlessEqual(1,c2.getGrowthrate())
        self.failUnlessEqual(0,c2.getOwner())
        self.failUnlessEqual(3,c2.getSize())
        self.failUnlessEqual(11, c2.getX())
        self.failUnlessEqual(11,c2.getY())
        
        notMyCamps = gs.getNotMyCamps()
        self.failUnlessEqual(3,len(notMyCamps))
        c2 = notMyCamps[0]  
        self.failUnlessEqual(1, c2.getID())
        self.failUnlessEqual(20,c2.getMancount())
        self.failUnlessEqual(40,c2.getMaxMancount())
        self.failUnlessEqual((1+20/20),c2.getGrowthrate())
        self.failUnlessEqual(2,c2.getOwner())
        self.failUnlessEqual(2,c2.getSize())
        self.failUnlessEqual(10, c2.getX())
        self.failUnlessEqual(10,c2.getY())
        
        production = gs.getProduction(2)
        self.failUnlessEqual(production,4)
        
        total = gs.getTotalMancount(2)
        self.failUnlessEqual(total,40)
        total = gs.getTotalMancount(1)
        self.failUnlessEqual(total,40)
        
        self.failUnlessEqual(True, gs.isAlive(1))
        self.failUnlessEqual(False, gs.isAlive(4))
        
        c2 = gs.getCamp(2)
        distance = gs.calculateDistance(c0, c1)
        self.failUnlessEqual(12,distance)
        distance = gs.calculateDistance(c0, c2)
        self.failUnlessEqual(13,distance)
        distance = gs.calculateDistance(c0, c3)
        self.failUnlessEqual(5,distance)
        
        src = gs.getCamp(0)
        dst = gs.getCamp(2)
        gs.issueOrder(src,dst, 2)
        self.failUnlessEqual(gs.getNumArmies(), 3)
        c0 = gs.getCamp(0)
        self.failUnlessEqual(18, c0.getMancount())
        
        print "--- Test upgradeCamp ---"
        gs.upgradeCamp(c0)
        print "------------------------"


#class IBot:
#    def doTurn(self, gamestate):
#    def getName(self):
#class Helper:
#    def executeBot(bot):



if __name__ == "__main__": 
    unittest.main()
