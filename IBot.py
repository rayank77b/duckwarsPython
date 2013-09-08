
class IBot:
    """Dieses Interface sollte vom Bot implementiert werden."""

    def doTurn(self, gamestate):
        """Wird aufgerufen wenn der nächste Zug durchgeführt werden kann. Der
           aktuelle Spielzustand wird dabei übergeben."""
        raise NotImplementedError("Please Implement this method")

    def getName(self):
        """Wird aufgerufen um den Namen des Bots abzufragen."""
        raise NotImplementedError("Please Implement this method")
