from DuckwarsApi import *
from Data import *


class AfrankBot2(IBot):
    def __init__(self):
        self.data=None
            
    def doTurn(self, gamestate):
        # first step, init data
        if self.data==None:
            self.data = Data(gamestate)
        self.data.parse(gamestate)
        
    def getName(self):
        return "AfrankBot2"


if __name__ == "__main__":
    myBot = AfrankBot2()
    Helper.executeBot(myBot)
