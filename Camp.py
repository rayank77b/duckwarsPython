class Camp:
    """Repräsentiert ein Camp."""

    def __init__(self,id, campOwner, campMancount, campSize, posX, posY):
        """Konstruktor"""
        self.__id = id
        self.__owner = campOwner
        self.__mancount = campMancount
        if (campSize < 1):
            campSize = 1
        if (campSize > 5)
            campSize = 5
        self.__size = campSize
        self.__x = posX
        self.__y = posY
    
    def getID(self):
        """Liefert die ID des Camps. """
        return self.__id
    
    def getMancount(self):
        """Liefert die Mannstärke des Camps. """
        return self.__mancount
    
    def getMaxMancount(self):
        """Liefert die maximale Anzahl Männer die dieses Camp aufnehmen kann. """
        return self.__size * 20
    
    def getGrowthrate(self):
        """Liefert die Wachstumsrate um der die Anzahl Männer pro Runde steigt. """
        return 1 + self.__mancount/20
    
    def getOwner(self):
        """Liefert die ID des Spielers dem dieses Camp gehört. """
        return self.__owner
    
    def getSize(self):
        """Liefert die Größe des Camps (1-5). """
        return self.__size
    
    def getX(self):
        """Liefert die X-Koordinate des Camps """
        return self.__x
    
    def getY(self):
        """Liefert die Y-Koordinate des Camps. """
        return self.__y

