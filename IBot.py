
class IBot:
    """Dieses Interface sollte vom Bot implementiert werden."""

    def doTurn(self, gamestate):
        """Wird aufgerufen wenn der naechste Zug durchgefuehrt werden kann. Der
           aktuelle Spielzustand wird dabei uebergeben."""
        raise NotImplementedError("Please Implement this method")

    def getName(self):
        """Wird aufgerufen um den Namen des Bots abzufragen."""
        raise NotImplementedError("Please Implement this method")
