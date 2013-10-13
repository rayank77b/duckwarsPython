from Distances import *

class Strategie:
    ''' Strategie is the father of all, it should only get iterators for all 
        possible return of Camps/Armies'''
    def __init__(self, gamestate, distances, debug=True):
        self.gs=gamestate
        self.dist=distances
        self.debug=debug
        if self.debug:
            self.log=open('/tmp/bot.log', 'a')
        else:
            self.log=None
    
    def logme(self, msg):
        ''' Debuging '''
        if self.debug:
            self.log.write(msg)
            self.log.flush()
    
    def getMyFullCamps(self):
        ''' generate all my full camp'''
        for c in self.gs.getMyCamps():
            if c.getMancount()>(c.getMaxMancount()-2):
                yield c

    def getNextEnemy(self, c):
        '''get the nearest enemy'''
        enemies=self.gs.getHostileCamps()
        return self.dist.getNearestCamp(c.getID(), enemies)
    
    def getNearestNeutralCamps(self, camp, radius=5):
        ''' generate all neutral camps about camp in radius r'''
        for c in self.gs.getNeutralCamps():
            if self.dist.get(camp.getID(),c.getID())<=(radius*radius):
                yield c
    
    def calculate(self):
        '''calculate shold calculate where and how many should be sent
           should return true if send something or false if nothing sended.'''
        raise NotImplementedError("Please Implement this method")
