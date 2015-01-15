from DuckwarsApi import *
from Distances import *
from ABStrategies import *
from ABCampInfo import *

import math
import time

__author__ = "Andrej Frank"
__copyright__ = "Copyright 2014, IT-Designers"
__license__ = "GPL"
__version__ = "4.0.3"
__maintainer__ = "Andrej Frank"
__email__ = "andrej.frank@stz-softwaretechnik.de"
__status__ = "Beta"

class AfrankBot1(IBot):
    def __init__(self):
        self.firstTurn = True
        self.distances = None
        self.gamestate = None
        self.DEBUG = False
        self.campInfo = None
        if self.DEBUG == True:
            self.f = open("/tmp/afrankbotlog.txt", 'a')
    
    def doTurn(self, gamestate):
        self.gamestate = gamestate
        if(self.firstTurn):
        # berechne alles, was statisch ist, bzw welche map, welche strategie
            allcamps=gamestate.getCamps()
            self.distances = Distances(allcamps)
            self.firstTurn = False
            self.campInfo = CampInfo(allcamps, gamestate)
            self.start()
        else:
            self.start()
        
    def start(self):
        """ the main game routine """
        if self.campInfo.allAreMaxSize():  # map 06.txt
            #self.logme("map 06 strategy")
            strategyFull(self.gamestate, self.distances, self)
        else:
            #self.logme("other strategy")
            strategySmall(self.gamestate, self.distances, self)
        
                    
    def logme(self, message):
        if self.DEBUG == True:
            self.f.write(message+"\n")
            self.f.flush()


    def getName(self):
        return "AfrankBotV04|PythonTeam"


if __name__ == "__main__":
    myBot = AfrankBot1()
    Helper.executeBot(myBot)
