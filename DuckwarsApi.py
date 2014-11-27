import sys
import os
import math

__author__ = "Kevin Erath, Andrej Frank, etc"
__copyright__ = "Copyright 2014, IT-Designers"
__license__ = "GPL"
__version__ = "2.0.0"
__maintainer__ = "Andrej Frank"
__email__ = "andrej.frank@stz-softwaretechnik.de"
__status__ = "Beta"

class Camp:
    """Repraesentiert ein Camp."""

    def __init__(self,id, campOwner, campMancount, campSize, posX, posY, state):
        """Konstruktor"""
        self.__id = id
        self.__owner = campOwner
        self.__mancount = campMancount
        if (campSize < 1):
            campSize = 1
        if (campSize > state.getSettings().MaxCampSize):
            campSize = state.getSettings().MaxCampSize
        self.__size = campSize
        self.__x = posX
        self.__y = posY
        self.__gameState = state

    def getID(self):
        """Liefert die ID des Camps. """
        return self.__id
    
    def getMancount(self):
        """Liefert die Mannstaerke des Camps. """
        return self.__mancount

    def setMancount(self, count):
        """Aendert die Mannstaerke des Camps."""
        self.__mancount = count
        
    def getMaxMancount(self):
        """Liefert die maximale Anzahl Maenner die dieses Camp aufnehmen kann. """
        return self.__gameState.getSettings().MaxManCount[self.__size - 1]

    def getMaxGrowthrate(self):
        """Liefert die maximale Wachstumsrate der die Anzahl Maenner pro Runde in diesem Camp steigen kann."""
        return self.__gameState.getSettings().GrowthRate[size - 1]

    def getGrowthrate(self):
        """Liefert die Wachstumsrate um der die Anzahl Maenner pro Runde steigt. """
        if (self.__mancount < self.getMaxMancount()):
            x = self.__gameState.getSettings().MaxCampSize - 2
            for i in range(x,0,-1):
                if (self.__mancount >= self.__gameState.getSettings().MaxManCount[i - 1]):
                    return self.__gameState.getSettings().GrowthRate[i]
            return self.__gameState.getSettings().GrowthRate[0]
        if (self.__mancount > self.getMaxMancount()):
            return -self.__gameState.getSettings().OverfullCampDecreseRate
        return 0

    def getUpgradeCost(self):
        """Aufruestkosten ermitteln"""
        if (self.__size < self.__gameState.getSettings().MaxCampSize):
            return self.__gameState.getSettings().UpgradeCost[self.__size - 1]
        return -1

    def getCanBeUpgraded(self):
        """Kann ein Camp aufgeruestet werden?"""
        return (size < self.__gameState.getSettings().MaxCampSize) and (self.__mancount >= self.getUpgradeCost())

    def getOwner(self):
        """Liefert die ID des Spielers dem dieses Camp gehoert. """
        return self.__owner
    
    def getSize(self):
        """Liefert die Groesse des Camps (1-5). """
        return self.__size

    def setSize(self, newSize):
        """Setzt die Groesse des Camps (1-5)."""
        self.__size = newSize

    def getX(self):
        """Liefert die X-Koordinate des Camps """
        return self.__x
    
    def getY(self):
        """Liefert die Y-Koordinate des Camps. """
        return self.__y

    ## fuer Testzwecken.
    def __str__(self):
        return "Camp id:%d owner:%d man:%d size:%d (%d:%d)"%(self.__id,self.__owner,self.__mancount,self.__size,self.__x, self.__y)


class Army:
    """Repraesentiert eine Armee die auf dem Weg zu einem anderen Camp ist."""

    def __init__(self, armyOwner, armySize, armySource, armyDestination, tripLength, remaining):
        """Konstruktor"""
        self.__owner = armyOwner
        self.__mancount = armySize
        self.__source = armySource
        self.__destination = armyDestination
        self.__turnsRemaining = remaining
        self.__tripDuration = tripLength
        
    def getDestination(self):
        """Liefert die ID des Zielcamps."""
        return self.__destination
    
    def getMancount(self):
        """Liefert die Mannstaerke der Armee."""
        return self.__mancount
    
    def getOwner(self):
        """Liefert den Spieler dem die Armee gehoert. """
        return self.__owner
    
    def getSource(self):
        """Liefert die ID des Ausgangscamps. """
        return self.__source
    
    def getTripDuration(self):
        """Liefert die Reisedauer. """
        return self.__tripDuration

    def getTurnsRemaining(self):
        """Liefert die verbleibende Reisezeit. """
        return self.__turnsRemaining

################################################################################
#
class GameSettings:
    """Enthaelt die Einstellungen fuer das laufende Spiel."""
    
    def __init__(self):
        self.MaxCampSize = 5;
        self.GrowthRate = [1, 2, 3, 4, 5]
        self.MaxManCount = [20, 40, 60, 80, 100]
        self.UpgradeCost = [10, 30, 50, 70]
        self.TravelCost = 1
        self.TravelCostStartsWithTurn = 7
        self.OverfullCampDecreseRate = 1
        self.MaxGameLength=0

    @staticmethod
    def fromDataString(dataString):
        """ extract Data from Strings and generate a GameSettings object."""
        x=0
        data = dataString.split(" ")
        settings = GameSettings()
        settings.MaxGameLength = int(data[x])
        x=x+1
        settings.OverfullCampDecreseRate = int(data[x])
        x=x+1
        settings.TravelCost = int(data[x])
        x=x+1
        settings.TravelCostStartsWithTurn = int(data[x])
        x=x+1
        settings.MaxCampSize = int(data[x]) 
        x=x+1
        for i in range(len(settings.MaxManCount)):    # 5x
            settings.MaxManCount[i] = int(data[x])
            x=x+1
        for i in range(len(settings.GrowthRate)): # 5x
            settings.GrowthRate[i] = int(data[x])
            x=x+1
        for i in range(len(settings.UpgradeCost)):  # 4x
            settings.UpgradeCost[i] = int(data[x]);
            x=x+1
        return settings

class GameState:
    """Diese Klasse repraesentiert den aktuellen Spielzustand."""
    
    def __init__(self, gameStateString, teamnames, settings):
        """Zur Initialisierung muss ein Spielzustandstring uebergeben werden."""
        self.__armies=[]
        self.__camps=[]
        self.__teamnames = teamnames
        self.__settings = settings
        self.__parseGameState(gameStateString)

    def getTeamNames(self):
        """Liefert die Teamnamen zurueck."""
        return self.__teamnames

    def getSettings(self):
        """Liefert die fuer dieses Spiel geltenden Einstellungen."""
        return self.__settings

    def calculateDistance(self, source, destination):
        """Ermittelt den Abstand zwischen zwei Camps, aufgerundend zur naechsten
           hoeheren Ganzzahl. Diese Zahl gibt die Anzahl von Zuegen an die benoetigt
           wird um die Strecke zurueckzulegen."""
        dx = source.getX() - destination.getX();
        dy = source.getY() - destination.getY();
        return int(math.ceil(math.sqrt(dx * dx + dy * dy)))

    def calculateTravelCost(self, source, destination):
        """ Berechnet die Kosten die eine Reise zwischen den beiden Camps
            verursachen. Mit Kosten ist gemeint, dass ab einem bestimmten
            Zug die Entenarmee nach und nach schrumpft.
        """
        dist = self.calculateDistance(source, destination)
        cost = (dist - self.__settings.TravelCostStartsWithTurn) * self.__settings.TravelCost
        if (cost < 0):
            cost = 0
        return cost

    def finishTurn(self):
        """Beendet den aktuellen Zug."""
        print "go"
        sys.stdout.flush()
    
    def getArmy(self, id):
        """Ermittelt die Armee mit der uebergebenen ID. Die erste Armee beginnt dabei
           mit der 0. Achtung: Die ID kann sich von Zug zu Zug aendern, da sie nicht
           eindeutig vergeben wird. """
        return self.__armies[id];

    def getCamp(self, id):
        """Ermittelt das Camp mit der angegebenen ID. Das erste Camp beginnt dabei
           mit der 0. Die IDs sind fuer das ganze Match eindeutig. """
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
        """Ermittelt alle neutralen Camps. D.h. Camps die derzeit keinem Spieler gehoeren. """
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
        """Ermittelt die Anzahl Einheiten die ein Spieler pro Zug generiert/erhaelt. """
        prod=0
        for p in self.__camps:
            if( p.getOwner() == playerID ):
                prod = prod + p.getGrowthrate()
        return prod
    
    def getTotalMancount(self, playerID):
        """Ermittelt die maximale Truppenstaerke eines Spielers. Dabei werden alle
           Einheiten in dem Camps und unterwegs gezaehlt. """
        count=0
        for camp in self.__camps:
            if( camp.getOwner() == playerID ):
                count = count + camp.getMancount()
        for army in self.__armies:
            if( army.getOwner() == playerID ):
                count = count + army.getMancount()
        return count
    
    def isAlive(self, playerID):
        """Ermittelt ob ein Spieler noch am leben ist. """
        for p in self.__camps:
            if( p.getOwner() == playerID ):
                return True
        for f in self.__armies:
            if( f.getOwner() == playerID ):
                return True
        return False

    def issueOrder(self, source, dest, mancount):
        """Sendet eine Truppe von einem Camp zu einem anderen. Pro Zug koennen
           beliebig viele Truppenbewegungen gestartet werden. Eine Truppenbewegung
           kann nicht gestoppt oder geaendert werden. """
        source.setMancount(source.getMancount() - mancount)
        dist = self.calculateDistance(source, dest)
        self.__armies.append(Army(1, mancount, source.getID(), dest.getID(), dist, dist))
        print "MV %d %d %d"%(source.getID(), dest.getID(), mancount);
        sys.stdout.flush()

    def upgradeCamp(self, dest):
        """Ein Camp auf die naechste Stufe aufruesten."""
        dest.setMancount(dest.getMancount() - dest.getUpgradeCost())
        dest.setSize(dest.getSize() + 1)
        print "UP %d"%dest.getID()
        sys.stdout.flush()

    def __parseGameState(self, s):
        """Wird verwendet um den Spielstand zu parsen. """
        self.__camps=[]
        self.__armies=[]
        idCamp = 0
        lines = s.split("\n")[:-1]  # letzte leeres ding nicht liefern.
        for line in lines:
            tokens = line.split(" ")
            if( (len(tokens) == 6) or (len(tokens) == 7) ):
                if( "C" in tokens[0] ):
                    if( len(tokens) == 6 ):
                        x = int(tokens[1])
                        y = int(tokens[2])
                        owner = int(tokens[3])
                        mancount = int(tokens[4])
                        size = int(tokens[5])
                        self.__camps.append(Camp(idCamp, owner, mancount, size, x, y, self))
                        idCamp=idCamp+1
                elif( "A" in tokens[0] ):
                    if( len(tokens) == 7):
                        owner = int(tokens[1])
                        mancount = int(tokens[2])
                        source = int(tokens[3])
                        destination = int(tokens[4])
                        totalTripLength = int(tokens[5])
                        turnsRemaining = int(tokens[6])
                        self.__armies.append(Army(owner, mancount, source, destination, totalTripLength, turnsRemaining))

class IBot:
    """Dieses Interface sollte vom Bot implementiert werden."""

    def doTurn(self, gamestate):
        """Wird aufgerufen wenn der naechste Zug durchgefuehrt werden kann. Der
           aktuelle Spielzustand wird dabei uebergeben."""
        raise NotImplementedError("Please Implement this method")

    def getName(self):
        """Wird aufgerufen um den Namen des Bots abzufragen."""
        raise NotImplementedError("Please Implement this method")

# TODO: FIXME
class Helper:
    """Hilfsklasse welche die Verarbeitungsschleife implementiert."""
    @staticmethod
    def executeBot(bot):
        """Durch den Aufruf wird die Verarbeitungsschleife gestartet."""
        try:
            teamnames = ["", "", "", ""]  # 4 teamnames
            line = ""
            message = ""
            settings = GameSettings()
            line = sys.stdin.readline()
            while(line):
                if( "go" in line ):
                    gs = GameState(message, teamnames, settings)
                    bot.doTurn(gs)
                    gs.finishTurn()
                    message = ""
                elif( "name?" in line ):
                    print bot.getName()
                    sys.stdout.flush()
                elif( "TN" in line ):
                    teamname = line.split(":")[1].trim()
                    id = int(line[2, 3]) - 1;      ## FIXME
                    teamnames[id] = teamname;
                elif(line.startsWith("ENV")):
                    settings = GameSettings.fromDataString(line.env[4:].strip());  ## FIXME
                else:
                    message = message+line+os.linesep
                line=sys.stdin.readline()
        except Exception as e:
            sys.stderr.write("shit happens : ")
            print e
