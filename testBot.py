#!/usr/bin/env python
#
# simple test of classes and gamestate

import sys
import os

import unittest 

from DuckwarsApi import *
from AfrankBot1 import *
from Distances import *



def createGameState():
    message="C 2 2 1 40 3\nC 20 2 3 40 3\nC 2 20 4 40 3\nC 20 20 2 40 3\nC 5 2 0 5 1\nC 2 5 0 5 1\nC 5 5 0 15 1\nC 17 2 0 5 1\nC 20 5 0 5 1\nC 17 5 0 15 1\nC 2 17 0 5 1\nC 5 20 0 5 1\nC 5 17 0 15 1\nC 20 17 0 5 1\nC 17 20 0 5 1\nC 17 17 0 15 1\nC 11 6 0 25 2\nC 6 11 0 25 2\nC 16 11 0 25 2\nC 11 16 0 25 2\nC 11 11 0 50 3\n"
    gs = GameState(message)
    return gs

def createCamps(gs):
    camps=gs.getCamps()
    return camps

class DistancesClassTest(unittest.TestCase):
   
    def setUp(self):
        self.gs = createGameState()
        self.camps = createCamps(self.gs)
        self.dist = Distances(self.camps)
    
    def test_calculateDistance(self):
        c=self.camps
        d=self.dist
        self.failUnlessEqual(d.calculate(c[1], c[6]), 234)
        self.failUnlessEqual(d.get(1,6), 234)
        self.failUnlessEqual(d.getMin(6), 9)
        self.failUnlessEqual(d.getNearestId(6), 4)
        c1=d.getNextOtherCamp(self.gs, 6)
        self.failUnlessEqual(c1.getID(), 4)


if __name__ == "__main__": 
    unittest.main()
