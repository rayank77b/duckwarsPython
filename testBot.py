#!/usr/bin/env python
#
# simple test of classes and gamestate

import sys
import os
import time 

import unittest 

from DuckwarsApi import *

def createGameState():
    msgC="C 20 2 2 40 3\nC 18 2 0 40 3\nC 16 2 0 40 3\nC 14 2 0 40 3\nC 12 2 0 40 3\nC 10 2 0 40 3\nC 8 2 0 40 3\nC 6 2 0 40 3\nC 4 2 0 40 3\nC 2 2 1 42 3\nC 20 4 0 40 3\nC 4 4 0 40 3\nC 10 4 0 40 3\nC 2 4 1 60 3\nC 12 4 1 40 3\nC 16 4 0 40 3\nC 8 4 0 40 3\nC 18 4 0 40 3\nC 6 4 0 40 3\nC 14 4 0 40 3\nC 12 6 0 40 3\nC 8 6 0 40 3\nC 18 6 0 40 3\nC 10 6 0 40 3\nC 14 6 0 40 3\nC 4 6 0 40 3\nC 6 6 0 40 3\nC 20 6 0 40 3\nC 2 6 0 40 3\nC 16 6 0 40 3\nC 10 8 0 40 3\nC 4 8 0 40 3\nC 18 8 1 40 3\nC 16 8 0 40 3\nC 12 8 0 40 3\nC 14 8 0 40 3\nC 8 8 0 40 3\nC 20 8 0 40 3\nC 2 8 0 12 3\nC 6 8 0 12 3\nC 16 10 0 40 3\nC 2 10 4 40 3\nC 14 10 0 40 3\nC 12 10 0 40 3\nC 18 10 0 40 3\nC 10 10 0 40 3\nC 4 10 4 23 3\nC 20 10 0 40 3\nC 6 10 4 37 3\nC 8 10 0 40 3\nC 16 12 0 40 3\nC 4 12 4 40 3\nC 14 12 0 40 3\nC 6 12 4 38 3\nC 2 12 4 39 3\nC 20 12 1 40 3\nC 10 12 0 40 3\nC 12 12 0 40 3\nC 8 12 4 30 3\nC 18 12 0 40 3\nC 6 14 4 44 3\nC 2 14 4 35 3\nC 18 14 0 40 3\nC 8 14 4 34 3\nC 16 14 0 40 3\nC 14 14 0 40 3\nC 10 14 0 9 3\nC 12 14 0 40 3\nC 20 14 0 40 3\nC 4 14 4 37 3\nC 16 16 0 40 3\nC 10 16 4 87 3\nC 20 16 0 40 3\nC 2 16 4 46 3\nC 18 16 0 40 3\nC 14 16 0 40 3\nC 8 16 4 55 3\nC 6 16 4 61 3\nC 4 16 4 55 3\nC 12 16 0 40 3\nC 20 18 0 20 3\nC 14 18 0 40 3\nC 12 18 0 40 3\nC 10 18 4 50 3\nC 18 18 0 20 3\nC 8 18 4 58 3\nC 6 18 4 19 3\nC 4 18 4 58 3\nC 16 18 0 40 3\nC 2 18 4 36 3\nC 20 20 2 60 3\nC 16 20 0 40 3\nC 14 20 0 40 3\nC 12 20 0 8 3\nC 8 20 4 38 3\nC 6 20 4 41 3\nC 4 20 4 49 3\nC 2 20 4 38 3\nC 18 20 0 40 3\nC 10 20 4 35 3\n"
    msgC2="C 20 2 2 40 3\nC 18 2 0 40 3\nC 16 2 0 40 3\nC 14 2 0 40 3\nC 12 2 0 40 3\nC 10 2 0 40 3\nC 8 2 0 40 3\nC 6 2 0 40 3\nC 2 2 1 42 3\nC 20 4 0 40 3\nC 4 4 0 40 3\nC 10 4 0 40 3\nC 2 4 1 60 3\nC 12 4 1 40 3\nC 16 4 0 40 3\nC 8 4 0 40 3\nC 18 4 0 40 3\nC 6 4 0 40 3\nC 14 4 0 40 3\nC 12 6 0 40 3\nC 8 6 0 40 3\nC 18 6 0 40 3\nC 10 6 0 40 3\nC 14 6 0 40 3\nC 4 6 0 40 3\nC 6 6 0 40 3\nC 20 6 0 40 3\nC 2 6 0 40 3\nC 18 8 1 40 3\nC 2 10 4 40 3\nC 14 10 0 40 3\nC 12 10 0 40 3\nC 18 10 0 40 3\nC 10 10 0 40 3\nC 4 10 4 23 3\nC 20 10 0 40 3\nC 6 10 4 37 3\nC 8 10 0 40 3\nC 16 12 0 40 3\nC 4 12 4 40 3\nC 14 12 0 40 3\nC 6 12 4 38 3\nC 2 12 4 39 3\nC 20 12 1 40 3\nC 10 12 0 40 3\nC 12 12 0 40 3\nC 10 20 4 35 3\n"
    msgA ="A 2 30 0 6 22 2\nA 1 30 8 9 21 12\nA 4 27 96 9 8 1\nA 4 25 7 3 8 3\nA 4 29 8 6 9 6\nA 4 27 7 3 10 7\nA 4 28 6 6 5 3\nA 4 25 4 9 4 2\nA 4 100 9 8 3 1\nA 1 100 9 1 3 1\n"
    
    msgC3="C 2 2 1 40 3\nC 5 2 0 40 3\nC 6 2 2 40 3\nC 4 6 0 40 3\nC 4 4 0 40 3\nC 8 6 2 40 3\n"
    msgA3 ="A 2 30 2 1 5 1\nA 1 60 0 2 2 1\nA 2 75 5 4 5 2\n"
    message=msgC #+msgA
    settings = GameSettings()
    gs = GameState(message, ["A","B","C","D"],settings)
    return gs

def createCamps(gs):
    camps=gs.getCamps()
    return camps

class DataTest(unittest.TestCase):
    def setUp(self):
        self.gs = createGameState()
        self.camps = createCamps(self.gs)















        
if __name__ == "__main__": 
    unittest.main()
