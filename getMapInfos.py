#!/usr/bin/python

# generate Data about Maps


import os
import math


path = "sandbox/maps"

class Camp:
    def __init__(self, x, y, owner, cnt, size):
        self.x=int(x)
        self.y=int(y)
        self.owner=int(owner)
        self.cnt=int(cnt)
        self.size=int(size)
    
    def getDistance(self, c):
        dx = self.x - c.x
        dy = self.y - c.y
        return int(math.sqrt(dx * dx + dy * dy))
    
    def myCamp(self):
        return self.owner==1
    
    
    def __str__(self):
        return "Camp: (%d:%d) %d  [%d:%d]"%(self.x,self.y,self.owner, self.cnt, self.size)

def getCampList(filename):
    fo = open(filename, "r")
    camps=[]
    for line in fo.readlines():
        if "C" in line:
            line = line.rstrip()
            l = line.split(" ")
            camps.append(Camp(l[1],l[2],l[3],l[4],l[5]))
    fo.close()
    return camps

def getCountMyCamps(camps):
    cnt=0
    for c in camps:
        if c.myCamp():
            cnt=cnt+1
    return cnt

def getMaxXY(camps):
    x=0
    y=0
    for c in camps:
        if x < c.x:
            x=c.x
        if y < c.y:
            y=c.y
    return x,y

def getLens(camps):
    lens=[]
    for c1 in camps:
        for c2 in camps:
            l=c1.getDistance(c2)
            if l>0:
                lens.append(l)
    return lens

def getVerteilungNormiert(lens):
    ma = max(lens)
    t=[0]*11
    for l in lens:
        x = int(l*10.0/ma)
        if x>10:
            x=10
        t[x]=t[x]+1
    return t

def getVerteilung(lens):
    ma = max(lens)
    t=[0]*11
    for l in lens:
        x = int(l)
        if x>10:
            x=10
        t[x]=t[x]+1
    return t



def getInfo(filename):
    #print(filename)
    camps = getCampList(filename)
    myCnt = getCountMyCamps(camps)
    campsCount=len(camps)
    print filename,":  camps: ", campsCount,":    myCamps: ",myCnt, " %2.0f %%"%((myCnt*100.0)/campsCount)
    lens = getLens(camps)
    mx, my = getMaxXY(camps)
    print "max X: ", mx, "   max Y: ", my
    print "midle length: ", sum(lens)/len(lens)
    print "max   length: ", max(lens)
    print "min   length: ", min(lens)
    print "vert : ", getVerteilung(lens)
    print "vert : ", getVerteilungNormiert(lens)
    #print lens
    print




# main loop
getInfo("sandbox/maps/24.txt")
#for root, dirs, files in os.walk(path, topdown=False):
#    for name in files:
#        filename = os.path.join(root, name)
#        getInfo(filename)



