
def generateAttack(mcs, distances, gamestate, divisor):
    for mc in mcs:
        a = [0]*(gamestate.getNumCamps()+1)
        a[0] = mc.id
        if mc.cnt > mc.max-3:
            other = distances.getClosestOtherCamp(gamestate, mc.id)
            if other != None:
                a[other.getID()] = mc.cnt/divisor
        mcs.simulation.append(a)
    return attack

class myCamp():
    def __init__(self, myid, cnt, maxman, upgradeable, grrate):
        self.id = myid
        self.cnt = cnt
        self.max = maxman
        self.attackme = []
        self.help = []
        self.upgradeable = upgradeable
        self.grrate = grrate
        self.simulation = []
    
    def appendArmy(self, armies):
        for a in armies:
            if a.getDestination() == self.id:
                if a.getOwner() == 0: # my army is help
                    self.help.append((a.getMancount(), a.getTurnsRemaining()))
                else:
                    self.attackme.append((a.getMancount(), a.getTurnsRemaining()))

   
    def appendAttack(self, men, rounds):
        self.attackme.append((men, rounds))
    
    def appendHelp(self, men, rounds):
        self.help.append((men, rounds))
