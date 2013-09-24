<?php
include('DuckwarsApi.php');

class phpBot implements IBot {

    /**
     * Wird aufgerufen wenn der nächste Zug durchgeführt werden kann. Der
     * aktuelle Spielzustand wird dabei übergeben.
     */
    public function doTurn($gamestate)
    {
        $cnt = $gamestate->getNumCamps();
        
        for($i=0; $i<$cnt; $i++) 
        {
            $c1=$gamestate->getCamp($i);
            if($c1->getOwner()==1)
            {
                if($c1->getMancount()>15)
                {
                    if(($i+1)<$cnt)
                        $gamestate->issueOrder($c1, $gamestate->getCamp($i+1), 5);
                    else
                        $gamestate->issueOrder($c1, $gamestate->getCamp(0), 5);
                }
            }
        }
    }

    /**
     * Wird aufgerufen um den Namen des Bots abzufragen.
     */
    public function getName()
    {
        return "phpBot1.0";
    }    
}

// main
$bot = new phpBot();
Helper::executeBot($bot);


?>
