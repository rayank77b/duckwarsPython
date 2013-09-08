from Camp import *
from Army import *
import sys

class GameState:
    """Diese Klasse repräsentiert den aktuellen Spielzustand."""

    def __init__(self, gameStateString):
        """Zur Initialisierung muss ein Spielzustandstring übergeben werden."""
        self.__armies=[]
        self.__camps=[]
        __parseGameState(gameStateString)


    def calculateDistance(source, destination):
        """Ermittelt den Abstand zwischen zwei Camps, aufgerundend zur nächsten
           höheren Ganzzahl. Diese Zahl gibt die Anzahl von Zügen an die benötigt
           wird um die Strecke zurückzulegen."""
        dx = source.getX() - destination.getX();
        dy = source.getY() - destination.getY();
        return (int) Math.ceil(Math.sqrt(dx * dx + dy * dy));
    

    def finishTurn(self):
        """Beendet den aktuellen Zug."""
        print "go"
        sys.stdout.flush()
    
    def getArmy(self, id):
        """Ermittelt die Armee mit der übergebenen ID. Die erste Armee beginnt dabei
           mit der 0. Achtung: Die ID kann sich von Zug zu Zug ändern, da sie nicht
           eindeutig vergeben wird. """
        return self.__armies[id];
        
    def getCamp(self, id):
        """Ermittelt das Camp mit der angegebenen ID. Das erste Camp beginnt dabei
           mit der 0. Die IDs sind für das ganze Match eindeutig. """
        return self.__camps[id];
    
    def getCamps(self):
        """Liefert eine Liste aller Camps. """
        return self.__camps
    
    def getHostileCamps(self):
        """Ermittelt alle Camps der gegnerischen Spieler. D.h. die eigenen und
           neutralen Camps sind nicht enthalten. """
        r = []
        for p in self.__camps:
            if(p.getOwner() >=2):
                r.append(p)
        return r
    
    def getMyArmies(self):
        """Ermittelt alle eigenen Truppen. """
        r = []
        for army in self.__armies:
            if (army.getOwner() == 1):
                r.append(army)
        return r
    
    def getMyCamps(self):
        """Ermittelt alle eigenen Camps. """
        r = []
        for p in self.__camps:
            if(p.getOwner() == 1):
                r.append(p)
        return r

    def getNeutralCamps(self):
        """Ermittelt alle neutralen Camps. D.h. Camps die derzeit keinem Spieler gehören. """
        r = []
        for p in self.__camps:
            if(p.getOwner() == 0):
                r.append(p)
        return r
    
    def getNotMyCamps(self):
        """Ermittelt alle Camps die derzeit nicht in der Hand des Spielers sind. """
        r = []
        for p in self.__camps:
            if(p.getOwner() != 1):
                r.append(p)
        return r

    def getNumArmies(self):
        """Liefert die Anzahl aller aktiven Armeen. """
        return len(self.__armies)
    
    def getNumCamps(self):
        """Liefert die Anzahl aller Camps. """
        return len(self.__camps)
    
    def getProduction(self, playerID):
        """Ermittelt die Anzahl Einheiten die ein Spieler pro Zug generiert/erhält. """
        prod=0
        for p in self.__camps:
            if( p.getOwner() == playerID ):
                prod = prod + p.getGrowthrate()
        return prod
    
    def getTotalMancount(self, playerID):
        """Ermittelt die maximale Truppenstärke eines Spielers. Dabei werden alle
           Einheiten in dem Camps und unterwegs gezählt. """
        count=0
        for camp in self.__camps:
            if( camp.getOwner() == playerID ):
                count = count + camp.getMancount()
        for army in self.armies:
            if( army.getOwner() == playerID ):
                count = count + army.getMancount()
        return count
    
    def isAlive(self, playerID):
        """Ermittelt ob ein Spieler noch am leben ist. """
        for p in self.__camps:
            if( p.getOwner() == playerID ):
                return True:
        for f in self.__armies:
            if( f.getOwner() == playerID ):
                return True
        return False
    
    def issueOrder(self, source, dest, mancount):
        """Sendet eine Truppe von einem Camp zu einem anderen. Pro Zug können
           beliebig viele Truppenbewegungen gestartet werden. Eine Truppenbewegung
           kann nicht gestoppt oder geändert werden. """
        print "%d %d %d"%(source.getID(), dest.getID(), mancount);
        sys.stdout.flush()
    
    def parseGameState(self, s):
        """Wird verwendet um den Spielstand zu parsen. """
        self.__camps=[]
        self.__armies=[]
        id = 0
        lines = s.split("\n")[:-1]  # letzte leeres ding nicht liefern.
        for line in lines:
            tokens = line.split(" ")
            if( (len(tokens) != 6) or (len(tokens) != 7) ):
                continue
            if( "C" in tokens[0] ):
                if( len(tokens) == 6 ):
                    x = (int)tokens[1]
                    y = (int)tokens[2]
                    owner = (int)tokens[3]
                    mancount = (int)tokens[4]
                    size = (int)tokens[5]
                    self.camps.append(Camp(id++, owner, mancount, size, x, y))
            elif( "A" in tokens[0] ):
                if( len(tokens) == 7):
                    owner = (int)tokens[1]
                    mancount = (int)tokens[2]
                    source = (int)tokens[3]
                    destination = (int)tokens[4]
                    totalTripLength = (int)tokens[5]
                    turnsRemaining = (int)tokens[6]
                    self.armies.append(Army(owner, mancount, source, destination, totalTripLength, turnsRemaining))

