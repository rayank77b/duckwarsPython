from DuckwarsApi import *


class AfrankBot2(IBot):

    def __init__(self):
        self.firstTurn=True
        self.dist=None
    
    def doTurn(self, gamestate):
        pass
    
    def getName(self):
        return "AfrankBot2"


if __name__ == "__main__":
    myBot = AfrankBot2()
    Helper.executeBot(myBot)
