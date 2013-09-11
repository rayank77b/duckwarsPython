#!/usr/bin/env python
#
# simple test of classes and gamestate

import sys
import os

import unittest 

from DuckwarsApi import *
from AfrankBot1 import *

class AfrankBotTest(unittest.TestCase):
    def testcalculateDistance(self):
        #  = Camp(id, campOwner, campMancount, campSize, posX, posY)
        c1 = Camp(0,  1, 20, 5, 1, 1)
        c2 = Camp(1,  1, 20, 5, 5, 5)
        self.failUnlessEqual(calculateDistance(c1,c2),32)













if __name__ == "__main__": 
    unittest.main()
