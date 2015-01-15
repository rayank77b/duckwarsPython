#!/usr/bin/python

# generate Data about Maps


import os
import math


path = "sandbox/maps"

################################################################################
# aehnliche classe
class Camp:
    def __init__(self,id, campOwner, campMancount, campSize, posX, posY, state):
        self.__x=int(posX)
        self.__y=int(posY)
        self.__owner=int(campOwner)
        self.__mancount=int(campMancount)
        self.__size=int(campSize)
        
    def getMancount(self):
        return self.__mancount

    def getOwner(self):
        return self.__owner
    
    def getSize(self):
        return self.__size

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
        
    def __str__(self):
        return "Camp: (%d:%d) %d  [%d:%d]"%(self.__x,self.__y,self.__owner, self.__mancount, self.__size)

class GameState:
    def __init__(self, gameStateString, teamnames, settings):
        self.__t = teamnames

    def calculateDistance(self, source, destination):
        dx = source.getX() - destination.getX();
        dy = source.getY() - destination.getY();
        return int(math.ceil(math.sqrt(dx * dx + dy * dy)))
################################################################################

# einlesen
#C 11 3 0 5 2
#C X  Y Own cnt size

def getCampList(filename, gs):
    fo = open(filename, "r")
    camps=[]
    ids=0
    for line in fo.readlines():
        if "C" in line:
            line = line.rstrip()
            t, x, y, o, c, s = line.split(" ")
            camps.append(Camp(ids,o,c,s,x,y,None))
            ids=ids+1
    fo.close()
    return CampInfo(camps, gs)

class CampInfo:
    def __init__(self, camps, gs):
        self.gs = gs
        self.camps = camps
        self.myCampCount=0
        self.maxX=0
        self.maxY=0
        self.minlens=[]
        self.lens=[]
        for c in self.camps:
            if self.maxX < c.getX():
                self.maxX=c.getX()
            if self.maxY < c.getY():
                self.maxY=c.getY()
            if c.getOwner()==1:
                self.myCampCount=self.myCampCount+1
            ml=99999
            for d in self.camps:
                l = self.gs.calculateDistance(c,d)
                if l!=0:
                    self.lens.append(l)
                    if l<ml:
                        ml=l
            self.minlens.append(ml)
        self.mml = 1.0*sum(self.minlens)/len(self.minlens)
        self.ml = math.sqrt(self.maxX*self.maxY/len(self.camps))
        self.coe = self.ml/self.mml
        
    def getCampsCount(self):
        return len(self.camps)

    def getMyCampsCount(self):        
        return self.myCampCount

    def getMaxXY(self):
        return self.maxX,self.maxY

    def getMinLens(self):
        return self.minlens

    def getLens(self):
        return self.lens

    def getVerteilungNormiertMin(self):
        ma = max(self.minlens)
        t=[0]*11
        for l in self.minlens:
            x = int(l*10.0/ma)
            if x>10:
                x=10
            t[x]=t[x]+1
        return t

    def getVerteilungMin(self):
        ma = max(self.minlens)
        t=[0]*11
        for l in self.minlens:
            x = int(l/10.0)
            if x>10:
                x=10
            t[x]=t[x]+1
        return t

    def getMidleLen(self, minlen):
        return self.ml

    def allAreMaxSize(self):
        yes = False
        return yes
    
    def out(self):
        campsCount = len(self.camps)
        print "camps: ", campsCount,":    myCamps: ", self.myCampCount, " %2.0f %%"%((self.myCampCount*100.0)/campsCount)
        print "max X: ", self.maxX, "   max Y: ", self.maxY
        print "vert : ", self.getVerteilungMin()
        print "vert : ", self.getVerteilungNormiertMin()
        print "midle length: ", sum(self.lens)/len(self.lens)
        print "max   length: ", max(self.lens)
        print "min   length: ", min(self.lens)
        print "midle min len: ", self.minlens
        print "mm len: %.2f"%self.mml
        print "midle Len: %.2f"%self.ml
        print "coefizent: %.2f"%self.coe

def getInfo(filename):
    #print(filename)
    gs = GameState( "blub", [], "ENV 23")
    campInfo = getCampList(filename, gs)
    print filename
    campInfo.out()
    print




# main loop
getInfo("sandbox/maps/01.txt")
getInfo("sandbox/maps/06.txt")
getInfo("sandbox/maps/12.txt")
#getInfo("sandbox/maps/25.txt")
#getInfo("sandbox/maps/59.txt")
#for root, dirs, files in os.walk(path, topdown=False):
#    for name in files:
#        filename = os.path.join(root, name)
#        getInfo(filename)



