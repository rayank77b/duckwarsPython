class Camp:
    """Repraesentiert ein Camp."""

    def __init__(self,id, campOwner, campMancount, campSize, posX, posY):
        """Konstruktor"""
        self.__id = id
        self.__owner = campOwner
        self.__mancount = campMancount
        if (campSize < 1):
            campSize = 1
        if (campSize > 5):
            campSize = 5
        self.__size = campSize
        self.__x = posX
        self.__y = posY
    
    def getID(self):
        """Liefert die ID des Camps. """
        return self.__id
    
    def getMancount(self):
        """Liefert die Mannstaerke des Camps. """
        return self.__mancount
    
    def getMaxMancount(self):
        """Liefert die maximale Anzahl Maenner die dieses Camp aufnehmen kann. """
        return self.__size * 20
    
    def getGrowthrate(self):
        """Liefert die Wachstumsrate um der die Anzahl Maenner pro Runde steigt. """
        return 1 + self.__mancount/20
    
    def getOwner(self):
        """Liefert die ID des Spielers dem dieses Camp gehoert. """
        return self.__owner
    
    def getSize(self):
        """Liefert die Groesse des Camps (1-5). """
        return self.__size
    
    def getX(self):
        """Liefert die X-Koordinate des Camps """
        return self.__x
    
    def getY(self):
        """Liefert die Y-Koordinate des Camps. """
        return self.__y

    ## fuer Testzwecken.
    def __str__(self):
        return "Camp id:%d owner:%d man:%d size:%d (%d:%d)"%(self.__id,self.__owner,self.__mancount,self.__size,self.__x, self.__y)
