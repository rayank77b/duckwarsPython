
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

