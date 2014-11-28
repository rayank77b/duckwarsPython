class Distances():
    def __init__(self, camps):
        """ Constructor
            calculate for all camps an array [][], ditances.
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

    def getMin(self, id):
        """ return the distance of two camps"""
        return min(self.distances[id])
    
    def getNearestId(self, id):
        """return the id of the nearest capmp with id"""
        m = min(self.distances[id])
        return self.distances[id].index(m)

    def getNextOtherCamp(self, gs, id):
        """ return the id of the neares camp, which not belong to me"""
        ocs = gs.getNotMyCamps()
        return self.getNearestCamp(id, ocs)
        
    def getNearestCamp(self, id, camps):
        """ return the id of the neares camp, which not belong to me"""
        c=None
        dis=9999999
        #print distances
        for o in camps:
            d = self.get(id, o.getID())
            if d<dis :
                dis=d
                c=o
        return c

