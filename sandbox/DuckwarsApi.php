<?php

/**
 * Diese Klasse repräsentiert den aktuellen Spielzustand.
 */
class GameState
{
    private $armies;
    private $camps;

    /**
     * Zur Initialisierung muss ein Spielzustandstring übergeben werden.
     */
    function GameState($gameStateString)
    {
        $this->camps = array();
        $this->armies = array();
        $this->parseGameState($gameStateString);
    }

    /**
     * Ermittelt den Abstand zwischen zwei Camps, aufgerundend zur nächsten
     * höheren Ganzzahl. Diese Zahl gibt die Anzahl von Zügen an die benötigt
     * wird um die Strecke zurückzulegen.
     */
    function calculateDistance($source, $destination)
    {
        $dx = $source->getX() - $destination->getX();
        $dy = $source->getY() - $destination->getY();
        return intval(ceil(sqrt($dx * $dx + $dy * $dy)));
        
    }

    /**
     * Beendet den aktuellen Zug.
     */
    function finishTurn()
    {
        echo "go".PHP_EOL;
        flush();
    }

    /**
     * Ermittelt die Armee mit der übergebenen ID. Die erste Armee beginnt dabei
     * mit der 0. Achtung: Die ID kann sich von Zug zu Zug ändern, da sie nicht
     * eindeutig vergeben wird.
     */
    function getArmy($id)
    {
        return $this->armies[$id];
    }

    /**
     * Ermittelt das Camp mit der angegebenen ID. Das erste Camp beginnt dabei
     * mit der 0. Die IDs sind für das ganze Match eindeutig.
     */
    function getCamp($id)
    {
        return $this->camps[$id];
    }

    /**
     * Liefert eine Liste aller Camps.
     */
    function getCamps()
    {
        return $this->camps;
    }

    /**
     * Ermittelt alle Camps der gegnerischen Spieler. D.h. die eigenen und
     * neutralen Camps sind nicht enthalten.
     */
    function getHostileCamps()
    {
        $r = array();
        foreach ($this->camps as $i => $camp)
        {
            if ($camp->getOwner() >= 2)
            {
                array_push($r, $camp);
            }
        }
        return $r;
    }

    /**
     * Ermittelt alle eigenen Truppen.
     */
    function getMyArmies()
    {
        $r = array();
        foreach ($this->armies as $i => $army)
        {
            if ($army->getOwner() == 1)
            {
                array_push($r, $army);
            }
        }
        return $r;
    }

    /**
     * Ermittelt alle eigenen Camps.
     */
    function getMyCamps()
    {
        $r = array();
        foreach ($this->camps as $i => $camp)
        {
            if ($camp->getOwner() == 1)
            {
                array_push($r, $camp);
            }
        }
        return $r;
    }

    /**
     * Ermittelt alle neutralen Camps. D.h. Camps die derzeit keinem Spieler
     * gehören.
     */
    function getNeutralCamps()
    {
        $r = array();
        foreach ($this->camps as $i => $camp)
        {
            if ($camp->getOwner() == 0)
            {
                array_push($r, $camp);
            }
        }
        return $r;
    }

    /**
     * Ermittelt alle Camps die derzeit nicht in der Hand des Spielers sind.
     */
    function getNotMyCamps()
    {
        $r = array();
        foreach ($this->camps as $i => $camp)
        {
            if ($camp->getOwner() != 1)
            {
                array_push($r, $camp);
            }
        }
        return $r;
    }

    /**
     * Liefert die Anzahl aller aktiven Armeen.
     */
    function getNumArmies()
    {
        return count($this->armies);
    }

    /**
     * Liefert die Anzahl aller Camps.
     */
    function getNumCamps()
    {
        return count($this->camps);
    }

    /**
     * Ermittelt die Anzahl Einheiten die ein Spieler pro Zug generiert/erhält.
     */
    function getProduction($playerID)
    {
        $prod = 0;
        foreach ($this->camps as $i => $camp)
        {
            if ($camp->getOwner() == $playerID)
            {
                $prod = $prod + $camp->getGrowthrate();
            }
        }
        return $prod;
    }

    /**
     * Ermittelt die maximale Truppenstärke eines Spielers. Dabei werden alle
     * Einheiten in dem Camps und unterwegs gezählt.
     */
    function getTotalMancount($playerID)
    {
        $count = 0;
        foreach ($this->camps as $i => $camp)
        {
            if ($camp->getOwner() == $playerID)
            {
                $count = $count + $camp->getMancount();
            }
        }
        foreach ($this->armies as $i => $army)
        {
            if ($army->getOwner() == $playerID)
            {
                $count = $count + $army->getMancount();
            }
        }
        return $count;
    }

    /**
     * Ermittelt ob ein Spieler noch am leben ist.
     */
    function isAlive($playerID)
    {
        foreach ($this->camps as $i => $camp)
        {
            if ($camp->getOwner() == $playerID) { return TRUE; }
        }
        foreach ($this->armies as $i => $army)
        {
            if ($army->getOwner() == $playerID) { return TRUE; }
        }
        return FALSE;
    }

    /**
     * Sendet eine Truppe von einem Camp zu einem anderen. Pro Zug können
     * beliebig viele Truppenbewegungen gestartet werden. Eine Truppenbewegung
     * kann nicht gestoppt oder geändert werden.
     */
    function issueOrder($source, $dest, $mancount)
    {
        $source->setMancount($source->getMancount() - $mancount);
        $dist = $this->calculateDistance($source, $dest);
        array_push($this->armies, new Army(1, $mancount, $source->getID(), $dest->getID(), $dist, $dist));
        echo $source->getID()." ".$dest->getID()." ".$mancount.PHP_EOL;
        flush();
    }

    /**
     * Wird verwendet um den Spielstand zu parsen.
     */
    private function parseGameState($gamestring)
    {
        unset($this->camps);
        $this->camps=array();
        unset($this->armies);
        $this->armies=array();
        $id = 0;
        $lines = explode("\n",$gamestring);
        foreach ($lines as $i => $line)
        {
            $tokens = explode(" ", $line);
            if( (count($tokens)==6) or count($tokens)==7 ) 
            {
                if (strcmp($tokens[0],"C")==0)
                {
                    $x = intval($tokens[1]);
                    $y = intval($tokens[2]);
                    $owner = intval($tokens[3]);
                    $mancount = intval($tokens[4]);
                    $size = intval($tokens[5]);
                    array_push($this->camps, new Camp($id, $owner, $mancount, $size, $x, $y));
                    $id = $id+1;
                }
                elseif (strcmp($tokens[0],"A")==0)
                {
                    $owner = intval($tokens[1]);
                    $mancount = intval($tokens[2]);
                    $source = intval($tokens[3]);
                    $destination = intval($tokens[4]);
                    $totalTripLength = intval($tokens[5]);
                    $turnsRemaining = intval($tokens[6]);
                    array_push($this->armies, new Army($owner, $mancount, $source, $destination, $totalTripLength, $turnsRemaining));
                }
            }
        }
    }
}
################################################################################
/**
 * Repräsentiert eine Armee die auf dem Weg zu einem anderen Camp ist.
 */
class Army 
{
    private $destination=0;
    private $mancount=0;
    private $owner=0;
    private $source=0;
    private $tripDuration=0;
    private $turnsRemaining=0;

    /**
     * Konstruktor
     */
    function Army($armyOwner, $armySize, $armySource, $armyDestination, $tripLength, $remaining)
    {
        $this->owner = $armyOwner;
        $this->mancount = $armySize;
        $this->source = $armySource;
        $this->destination = $armyDestination;
        $this->turnsRemaining = $remaining;
        $this->tripDuration = $tripLength;
    }

    /**
     * Liefert die ID des Zielcamps.
     */
    function getDestination()
    {
        return $this->destination;
    }

    /**
     * Liefert die Mannstärke der Armee.
     */
    function getMancount()
    {
        return $this->mancount;
    }

    /**
     * Liefert den Spieler dem die Armee gehört.
     */
    function getOwner()
    {
        return $this->owner;
    }

    /**
     * Liefert die ID des Ausgangscamps.
     */
    function getSource()
    {
        return $this->source;
    }

    /**
     * Liefert die Reisedauer.
     */
    function getTripDuration()
    {
        return $this->tripDuration;
    }

    /**
     * Liefert die verbleibende Reisezeit.
     */
    function getTurnsRemaining()
    {
        return $this->turnsRemaining;
    }
}
################################################################################
/**
 * Repräsentiert ein Camp.
 */
class Camp
{
    private $id;
    private $mancount;
    private $owner;
    private $size;
    private $x;
    private $y;

    /**
     * Konstruktor
     */
    function Camp($id, $campOwner, $campMancount, $campSize, $posX, $posY)
    {
        $this->id = $id;
        $this->owner = $campOwner;
        $this->mancount = $campMancount;
        if ($campSize < 1)
        {
            $campSize = 1;
        }
        if ($campSize > 5)
        {
            $campSize = 5;
        }
        $this->size = $campSize;
        $this->x = $posX;
        $this->y = $posY;
    }

    /**
     * Liefert die ID des Camps.
     */
    function getID()
    {
        return $this->id;
    }

    /**
     * Liefert die Mannstärke des Camps.
     */
    function getMancount()
    {
        return $this->mancount;
    }
    
    /**
     * Ändert die Mannstärke des Camps.
     */
    function setMancount($count)
    {
        $this->mancount=$count;
    }

    /**
     * Liefert die maximale Anzahl Männer die dieses Camp aufnehmen kann.
     */
    function getMaxMancount()
    {
        return $this->size * 20;
    }
    
    /**
     * Liefert die Wachstumsrate um der die Anzahl Männer pro Runde steigt.
     */
    function getGrowthrate()
    {
        if ($this->owner == 0)
        {
            return 0;
        }
        if ($this->mancount == $this->getMaxMancount())
        {
            return 0;
        }
        if ($this->mancount > $this->getMaxMancount())
        {
            return -1;
        }
        return 1 + $this->mancount / 20;
    }

    /**
     * Liefert die ID des Spielers dem dieses Camp gehört.
     */
    function getOwner()
    {
        return $this->owner;
    }

    /**
     * Liefert die Größe des Camps (1-5).
     */
    function getSize()
    {
        return $this->size;
    }

    /**
     * Liefert die X-Koordinate des Camps.
     */
    function getX()
    {
        return $this->x;
    }

    /**
     * Liefert die Y-Koordinate des Camps.
     */
    function getY()
    {
        return $this->y;
    }
}
################################################################################
/**
 * Hilfsklasse welche die Verarbeitungsschleife implementiert.
 */
class Helper
{
    /**
     * Durch den Aufruf wird die Verarbeitungsschleife gestartet.
     */
    public static function executeBot($bot)
    {
        try
        {
            $message="";
            $line = trim(fgets(STDIN));
            while ($line >= 0)
            {
                if (strcmp($line,"go")==0)
                {
                    $pw = new GameState($message);
                    $bot->doTurn($pw);
                    $pw->finishTurn();
                    $message = "";
                }
                elseif (strcmp($line, "name?")==0)
                {
                    echo $bot->getName().PHP_EOL;
                    flush();
                }
                else
                {
                    $message = $message.$line.PHP_EOL;
                }
                
                $line = trim(fgets(STDIN));
            }
        }
        catch (Exception $e)
        {
            file_put_contents('php://stderr', $e->getMessage());
        }
    }
}
################################################################################
/**
 * Dieses Interface sollte vom Bot implementiert werden.
 */
interface IBot
{
    /**
     * Wird aufgerufen wenn der nächste Zug durchgeführt werden kann. Der
     * aktuelle Spielzustand wird dabei übergeben.
     */
    public function doTurn($gamestate);

    /**
     * Wird aufgerufen um den Namen des Bots abzufragen.
     */
    public function getName();
}


?>
