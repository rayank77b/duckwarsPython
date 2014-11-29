import random

from DuckwarsApi import *

class RndBot(IBot):
    def doTurn(self, gamestate):
        myCamps = gamestate.getMyCamps()
        maxCampCount = len(gamestate.getCamps())-1
        for src, myC in enumerate(myCamps):
            dst = random.randint(0,maxCampCount)
            if dst!=src:
                cnt = random.randint(1, myC.getMancount())
                hostile = gamestate.getCamp(dst)
                gamestate.issueOrder(myC, hostile, cnt)       

    def getName(self):
        return "RandBot|Python"


if __name__ == "__main__":
    myBot = RndBot()
    Helper.executeBot(myBot)

