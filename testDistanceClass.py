#!/usr/bin/env python
#
# simple test of classes and gamestate

import sys
import os
import time 
import unittest 
from Distances import *

class Camp:
    def __init__(self,x,y, owner):
        self.X=x
        self.Y=y
        self.owner=owner
    
    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    
    def getOwner(self):
        return self.owner
        

def createCamps():
    a=[]
    a.append(Camp(4, 4, 1))
    a.append(Camp(8, 4, 0))
    a.append(Camp(27, 4, 3))
    a.append(Camp(23, 4, 0))
    a.append(Camp(6, 7, 1))
    a.append(Camp(2, 7, 0))
    a.append(Camp(29, 7, 0))
    a.append(Camp(25, 7, 3))
    a.append(Camp(11, 9, 0))
    a.append(Camp(20, 9, 0))
    a.append(Camp(3, 10, 0))
    a.append(Camp(25, 10, 0))
    a.append(Camp(6, 10, 0))
    a.append(Camp(28, 10, 0))
    a.append(Camp(24, 14, 0))
    a.append(Camp(22, 14, 0))
    a.append(Camp(9, 14, 0))
    a.append(Camp(7, 14, 0))
    a.append(Camp(9, 17, 0))
    a.append(Camp(24, 17, 0))
    a.append(Camp(22, 17, 0))
    a.append(Camp(7, 17, 0))
    a.append(Camp(3, 21, 0))
    a.append(Camp(6, 21, 0))
    a.append(Camp(25, 21, 0))
    a.append(Camp(28, 21, 0))
    a.append(Camp(11, 22, 0))
    a.append(Camp(20, 22, 0))
    a.append(Camp(2, 24, 0))
    a.append(Camp(6, 24, 4))
    a.append(Camp(25, 24, 2))
    a.append(Camp(29, 24, 0))
    a.append(Camp(4, 27, 4))
    a.append(Camp(23, 27, 0))
    a.append(Camp(27, 27, 2))
    a.append(Camp(8, 27, 0))
    return a

class DistanceTest(unittest.TestCase):
    def testCamps(self):
        camps = createCamps()
        self.failUnlessEqual(len(camps),36)
        c =camps[2]
        self.failUnlessEqual(c.getX(),27)
        self.failUnlessEqual(c.getY(),4)
        self.failUnlessEqual(c.getOwner(),3)
        
    def testDistance(self):
        camps = createCamps()
        dists = Distances(camps)
        self.failUnlessEqual(dists.getMinDistance(4), 9)
        self.failUnlessEqual(dists.getClosestId(4), 12)
        reihe = dists.getList(4)
        print reihe
        i = reihe.index(min(reihe))
        print i
        reihe[i] = 99999999
        i = reihe.index(min(reihe))
        print i
        reihe[i] = 99999999
        i = reihe.index(min(reihe))
        print i
        reihe[i] = 99999999
        i = reihe.index(min(reihe))
        print i
        reihe[i] = 99999999
        
        














        
if __name__ == "__main__": 
    unittest.main()
