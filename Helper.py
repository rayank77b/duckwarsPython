import sys
import os

class Helper:
    """Hilfsklasse welche die Verarbeitungsschleife implementiert."""

    @staticmethod
    def executeBot(bot):
        """Durch den Aufruf wird die Verarbeitungsschleife gestartet."""
        try:
            line = ""
            message = ""
            line=sys.stdin.readline()
            while(line):
                if( "go" in line ):
                    ps = GameState(message)
                    bot.doTurn(pw)
                    pw.finishTurn()
                    message=""
                elif( "name?" in line ):
                    print bot.getName()
                    sys.stdout.flush()
                else:
                    message=message+line+os.linesep
                line=sys.stdin.readline()
        except Exception as e:
            sys.stderr.write("shit happens") #e.strerror)

