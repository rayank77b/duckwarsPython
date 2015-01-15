import random
import math

class CampInfo:
    def __init__(self, camps, gs):
        self.gs = gs
        self.camps = camps
        self.myCampCount=0
        self.maxX=0
        self.maxY=0
        self.minlens=[]
        self.lens=[]
        self.allMaxSize=True
        for c in self.camps:
            if c.getSize() < 5:
                self.allMaxSize=False
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
        return self.allMaxSize
