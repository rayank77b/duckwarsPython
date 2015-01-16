#!/usr/bin/python

# generate Data about Maps


import os
import math
from ABCampInfo import *

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
    
def out(ci):
    campsCount = len(ci.camps)
    print "camps: ", campsCount,":    myCamps: ", ci.myCampCount, " %2.0f %%"%((ci.myCampCount*100.0)/campsCount)
    print "max X: ", ci.maxX, "   max Y: ", ci.maxY
    print "vert : ", ci.getVerteilungMin()
    print "vert : ", ci.getVerteilungNormiertMin()
    print "midle length: ", sum(ci.lens)/len(ci.lens)
    print "max   length: ", max(ci.lens)
    print "min   length: ", min(ci.lens)
    print "midle min len: ", ci.minlens
    print "mm len: %.2f"%ci.mml
    print "midle Len: %.2f"%ci.ml
    print "coefizent: %.2f"%ci.coe
    print "all max size: ", ci.allMaxSize
#################################

# einlesen
#C 11 3 0 5 2
#C X  Y Own cnt size

def getCampList(filename, gs):
    liste=[]
    cntid=0
    fd = open(filename, "r")
    for line in fd.readlines():
        if "C" in line:
            line.strip()
            tmp,posX,posY, campOwner, campMancount, campSize = line.split(" ")
            #print tmp, posX, posY, campOwner, campMancount, campSize
            liste.append(Camp(cntid, campOwner, campMancount, campSize, posX, posY, gs))
            cntid=cntid+1
    fd.close()
    return liste

def getInfo(filename):
    #print(filename)
    gs = GameState( "blub", [], "ENV 23")
    campListe = getCampList(filename, gs)
    campInfo = CampInfo(campListe, gs)
    print filename
    out(campInfo)
    print




# main loop
#getInfo("sandbox/maps/01.txt")
getInfo("sandbox/maps/06.txt")
getInfo("sandbox/maps/12.txt")
getInfo("sandbox/maps/25.txt")
getInfo("sandbox/maps/59.txt")


#for root, dirs, files in os.walk(path, topdown=False):
#    for name in files:
#        filename = os.path.join(root, name)
#        getInfo(filename)



