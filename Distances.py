class Distances():
    """ build a matrix of all distances between all camps, 
        must be do one time in begin of game (first round)
        after the build ass search are staticaly and very fast"""
    def __init__(self, camps):
        """ calculate for all camps an array [][], ditances.
            the matrix has then the distances beetwen the camps"""
        self.camps_size=len(camps)
        self.distances= [[9999999 for col in range(self.camps_size)] for row in range(self.camps_size)]
        for x in range(self.camps_size):
            for y in range(self.camps_size):
                if(x!=y):
                    self.distances[x][y]=self.calculate(camps[x], camps[y])
                
    def calculate(self, s, d):
        dx = s.getX() - d.getX()
        dy = s.getY() - d.getY()
        return int(dx * dx + dy * dy)

    def out(self):
        for x in range(self.camps_size):
            print self.distances[x]

    def get(self, myid, campid):
        return self.distances[myid][campid]
    
    def getList(self, myid):
        return self.distances[myid][:]

    def getMinDistance(self, id):
        """ return the min Distances to camp with id. """
        return min(self.distances[id])
    
    def getClosestId(self, id):
        """return the id of the nearest capmp with id"""
        m = min(self.distances[id])
        return self.distances[id].index(m)
    
    def getClosestMyCamp(self, gs, id):
        """ return the id of the closest camp, which  belong to me"""
        ocs = gs.getMyCamps()
        c=None
        dis=9999999
        if len(ocs) == 1:
            return None
        for o in ocs:
            d = self.get(id, o.getID())
            if d<dis :
                dis=d
                c=o
        return c
            
    def getClosestOtherCamp(self, gs, id):
        """ return the id of the closest camp, which not belong to me"""
        ocs = gs.getNotMyCamps()
        c=None
        dis=9999999
        #print distances
        for o in ocs:
            d = self.get(id, o.getID())
            if d<dis :
                dis=d
                c=o
        return c
