import math

# This constants represent the indexes in camps and army array.
# Camp constants
C_X=0
C_Y=1
C_OWNER=2
C_CNT=3
C_SIZE=4
C_ARMY=5
C_DIST=6
# Army constants
A_OWNER=0
A_CNT=1
A_SRC=2
A_DST=3
A_TRIP=4
A_REM=5
#
S_ARMY=0
S_RET=1

def get_dist(x1, y1, x2, y2):
    ''' this is a simple and fast destanation length '''
    d = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
    if d == 0:
        return 9999999
    return d

class Data:
    '''Data store all data about camps (x,y,count, size..)
       and armies, which are incomming to camp. 
       the it store all distances to each camp.
       all datas are simple arrays'''
    def __init__(self, gs):
        ''' create an array of camps, calculate all distances'''
        self.camps=[]
        campslen = gs.getNumCamps()

        #print "Data campslen: ", campslen
        for id in range(campslen):
            c=[0,0,0,0,0,[],[]]
            camp=gs.getCamp(id)
            c[C_X]=camp.getX()
            c[C_Y]=camp.getY()
            c[C_OWNER]=camp.getOwner()  
            c[C_CNT]=camp.getMancount()
            c[C_SIZE]=camp.getSize()
            self.camps.append(c)
    
        for id in range(campslen):
            d=[]
            c=self.camps[id]
            for i in range(campslen):
                d.append(get_dist(c[C_X], c[C_Y], self.camps[i][C_X], self.camps[i][C_Y]))
            self.camps[id][C_DIST]=d

    def parse(self, gs):
        '''parse some changed parameters of camp and create armies arrays for each attacked camp'''
        campslen = gs.getNumCamps()
        armieslen = gs.getNumArmies()
        for id in range(campslen):
            camp=gs.getCamp(id)
            self.camps[id][C_OWNER]=camp.getOwner()
            self.camps[id][C_CNT]=camp.getMancount()
        for i in range(armieslen):
            a=[0,0,0,0,0,0]
            army=gs.getArmy(i)
            a[A_OWNER]=army.getOwner()
            a[A_CNT]=army.getMancount()
            a[A_SRC]=army.getSource()
            a[A_DST]=army.getDestination()
            a[A_TRIP]=army.getTripDuration()
            a[A_REM]=army.getTurnsRemaining()
            self.camps[a[A_DST]][C_ARMY].append(a)

    def getBest(self, bots):
        ret=None
        max=0
        for bot in bots:
            if max<bot.sum:
                max=bot.sum
                ret=bot
        return ret

    def __str__(self):
        camps=str(len(self.camps))+str(self.camps)
        return "camps: "+camps+"\n"



