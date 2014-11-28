from Army import *
from Camp import *
from GameState import *
from Helper import *

class VoidBot(IBot):
    def doTurn(self, gamestate):
        myCamp = gamestate.getMyCamps()[0]
        hostile = gamestate.getHostileCamps()[0]
        gamestate.issueOrder(myCamp, hostile, 5);
    
    def getName(self):
        return "Void Bot"


if __name__ == "__main__":
    myBot = VoidBot()
    Helper.executeBot(myBot)
