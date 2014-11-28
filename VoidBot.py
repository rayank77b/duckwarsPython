from DuckwarsApi import *

class VoidBot(IBot):
    def doTurn(self, gamestate):
        pass
        #myCamp = gamestate.getMyCamps()[0]
        #hostile = gamestate.getHostileCamps()[0]
        #gamestate.issueOrder(myCamp, hostile, 5);
    
    def getName(self):
        return "Void Bot|Bluber"


if __name__ == "__main__":
    myBot = VoidBot()
    Helper.executeBot(myBot)
