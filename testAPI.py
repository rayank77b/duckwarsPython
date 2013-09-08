#!/usr/bin/env python
#
# simple test of classes and gamestate

import sys
import os

import unittest 

from Army import *
from Camp import *
from GameState import *

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

class CampTest(unittest.TestCase):
    def testCamp(self):
        id=0
        campOwner=1
        campMancount=33
        campSize=5
        posX=5
        posY=7
        c = Camp(id, campOwner, campMancount, campSize, posX, posY)
        self.failUnlessEqual(c.getID(),id)
        self.failUnlessEqual(c.getMancount(),campMancount)
        self.failUnlessEqual(c.getMaxMancount(),campSize*20)
        self.failUnlessEqual(2,(1+campMancount/20))
        self.failUnlessEqual(c.getGrowthrate(),(1+campMancount/20))
        self.failUnlessEqual(c.getOwner(),campOwner)
        self.failUnlessEqual(c.getSize(),campSize)
        self.failUnlessEqual(c.getX(),posX)
        self.failUnlessEqual(c.getY(),posY)

class GameStateTest(unittest.TestCase):
    def testGameState(self):
        # C x y owner mancount size
		# A owner mancount source destination totaltrip turnRem
        mC1 = "C 2 2 1 20 3\n"   # id 0
        mC2 = "C 10 10 2 20 2\n" # id 1
        mC3 = "C 11 11 0 10 3\n" # id 2
        mC4 = "C 5 5 2 20 3\n"   # id 3
        mA1 = "A 1 10 0 1 10 5\n"
        mA2 = "A 1 10 0 2 10 5\n"
        message = mC1+mC2+mC3+mC4+mA1+mA2
        gs = GameState(message)
        self.failUnlessEqual(gs.getNumCamps(), 4)
        self.failUnlessEqual(gs.getNumArmies(), 2)
        
        a = gs.getArmy(0)
        self.failUnlessEqual(1,a.getDestination())
        self.failUnlessEqual(10,a.getMancount())
        self.failUnlessEqual(1,a.getOwner())
        self.failUnlessEqual(0,a.getSource())
        self.failUnlessEqual(10,a.getTripDuration())
        self.failUnlessEqual(5,a.getTurnsRemaining())
        
        
        c0 = gs.getCamp(0)
        c1 = gs.getCamp(1)
        c2 = gs.getCamp(2)
        c3 = gs.getCamp(3)
        self.failUnlessEqual(2, c2.getID())
        self.failUnlessEqual(10,c2.getMancount())
        self.failUnlessEqual(60,c2.getMaxMancount())
        self.failUnlessEqual((1+10/20),c2.getGrowthrate())
        self.failUnlessEqual(0,c2.getOwner())
        self.failUnlessEqual(3,c2.getSize())
        self.failUnlessEqual(11, c2.getX())
        self.failUnlessEqual(11,c2.getY())
        
        cs = gs.getCamps()
        self.failUnlessEqual(4, len(cs))
        c2 = cs[2]
        self.failUnlessEqual(2, c2.getID())
        self.failUnlessEqual(10,c2.getMancount())
        self.failUnlessEqual(60,c2.getMaxMancount())
        self.failUnlessEqual((1+10/20),c2.getGrowthrate())
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
        self.failUnlessEqual((1+10/20),c2.getGrowthrate())
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
        


if __name__ == "__main__": 
    unittest.main()
