class myCamp():
    def __init__(self, myid, cnt, maxman, upgradeable):
        self.id = myid
        self.cnt = cnt
        self.max = maxman
        self.attackme = []
        self.help = []
        self.upgradeable = upgradeable
    
    def appendArmy(self, armies)
        for a in armies:
            if a.getDestination() == self.id:
                self.attackme.append((a.getMancount(), a.getTurnsRemaining()))

   
    def appendAttack(self, men, rounds)
        self.attackme.append((men, rounds))
    
    def appendHelp(self, men, rounds)
        self.help.append((men, rounds))
