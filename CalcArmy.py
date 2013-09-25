import Data

class CalcArmy(object):
    ''' Interface for calculation of Army '''
    def calc(self):
        raise NotImplementedError( "Should have implemented this" )
    def getName(self):
        raise NotImplementedError( "Should have implemented this" )
