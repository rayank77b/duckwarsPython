#!/usr/bin/env python
#
# simple test of classes and gamestate

import sys
import os

import unittest 

from DuckwarsApi import *
from AfrankBot1 import *

def createCamps():
    camps=[]
    camps.append(Camp(0, 1,20,5,1,1))
    camps.append(Camp(1, 1,20,5,6,2))
    camps.append(Camp(2, 1,20,5,2,2))
    camps.append(Camp(3, 1,20,5,3,5))
    camps.append(Camp(4, 1,20,5,10,1))
    camps.append(Camp(5, 1,20,5,61,2))
    camps.append(Camp(6, 1,20,5,2,21))
    camps.append(Camp(7, 1,20,5,33,51))
    camps.append(Camp(8, 1,20,5,71,1))
    camps.append(Camp(9, 1,20,5,7,27))
    camps.append(Camp(10, 1,20,5,122,2))
    camps.append(Camp(11, 1,20,5,73,75))
    camps.append(Camp(12, 1,20,5,310,31))
    camps.append(Camp(13, 1,20,5,161,2))
    camps.append(Camp(14, 1,20,5,12,281))
    camps.append(Camp(15, 1,20,5,233,51))
    camps.append(Camp(16, 1,20,5,22,82))
    camps.append(Camp(17, 1,20,5,23,85))
    camps.append(Camp(18, 1,20,5,120,18))
    camps.append(Camp(19, 1,20,5,621,28))
    return camps

class AfrankBotTest(unittest.TestCase):
    def test_calculateDistance(self):
        #  = Camp(id, campOwner, campMancount, campSize, posX, posY)
        c1 = Camp(0,  1, 20, 5, 1, 1)
        c2 = Camp(1,  1, 20, 5, 5, 5)
        self.failUnlessEqual(calculateDistance(c1,c2),32)
        c2 = Camp(1,  1, 20, 5, 3, 5)
        self.failUnlessEqual(calculateDistance(c1,c2),(2*2+4*4))
        c2 = Camp(1,  1, 20, 5, 35, 55)
        self.failUnlessEqual(calculateDistance(c1,c2),(34*34+54*54))

    def test_calculateDistances(self):
        camps=createCamps()
        t1 = time.time()
        distances=calculateDistances(camps)
        t2 = time.time()
        dif = (t2-t1)*1000000
        print "%d us"%dif
        for d in distances:
            for x in d:
                if x==0:
                    print "oooo some zero",d
                    self.fail()

    def test_getMinDistance(self):
        camps=createCamps()
        distances=calculateDistances(camps)
        self.failUnlessEqual(getMinDistance(distances, 12),6329)
        self.failUnlessEqual(getMinDistance(distances, 1),16)
        self.failUnlessEqual(getMinDistance(distances, 2),2)
        self.failUnlessEqual(getNearestCamp(distances,8),5)
        self.failUnlessEqual(getNearestCamp(distances,9),6)

    def test_getNearestCamp(self):
        camps=createCamps()
        distances=calculateDistances(camps)
        self.failUnlessEqual(getNearestCamp(distances,19),12)
        self.failUnlessEqual(getNearestCamp(distances,15),12)
        self.failUnlessEqual(getNearestCamp(distances,12),15)
        self.failUnlessEqual(getNearestCamp(distances,3),2)
        self.failUnlessEqual(getNearestCamp(distances,10),18)
        self.failUnlessEqual(getNearestCamp(distances,18),10)
        self.failUnlessEqual(getNearestCamp(distances,1),2)








if __name__ == "__main__": 
    unittest.main()
