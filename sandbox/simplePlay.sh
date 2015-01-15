#java -jar duckwars.jar -sim maps/01.txt -mn results/test -ts 400 -c "java -jar SpawnBot.jar" -c "java -jar ModeBot.jar" -c "java -jar RndBot.jar" -c "python ../AfrankBot.py" -show
#java -jar duckwars.jar -sim maps/01.txt -mn results/test -ts 100 -c "java -jar SpawnBot.jar" -c "java -jar ModeBot.jar" -c "java -jar RndBot.jar" -show

MYBOT="python ../AB.py"
AFR="python ../AfrankBotV01.py"
SPAWN="java -jar SpawnBot.jar"
RND="java -jar RndBot.jar"

################################################################################
# 2 bots
echo "boot: 1   RND" > ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$RND" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 1   SPAWN" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$SPAWN" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 1   AFR" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$AFR" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done
################################################################################
# 3 bots
echo "boot: 2   RND RND" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$RND" -c "$RND" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 2   RND SPAWN" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$RND" -c "$SPAWN" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 2   RND AFR" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$RND" -c "$AFR" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 2   SPAWN SPAWN" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$SPAWN" -c "$SPAWN" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 2   SPAWN AFR" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$SPAWN" -c "$AFR" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 2   AFR AFR" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$AFR" -c "$AFR" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done
################################################################################
# 4 bots
echo "boot: 3   SPAWN SPAWN SPAWN" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$SPAWN" -c "$SPAWN" -c "$SPAWN" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 2   SPAWN SPAWN AFR" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$SPAWN" -c "$SPAWN" -c "$AFR" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 2   SPAWN AFR AFR" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$SPAWN" -c "$AFR" -c "$AFR" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

echo "boot: 2   AFR AFR AFR" >> ergebnis.txt
for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt
java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$AFR" -c "$AFR" -c "$AFR" #-show 
tail -n 1 results/test.erg >> ergebnis.txt
done

################################################################################



exit 0

for l in $(seq -w 1 60)
do
echo -n "map: $l  " >> ergebnis.txt

java -jar duckwars.jar -sim maps/$l.txt -mn results/test -ts 600 -c "$MYBOT" -c "$AFR" -c "$SPAWN" -c "$SPAWN" #-show 
tail -n 1 results/test.erg >> ergebnis.txt

done



exit 0

for l in $(seq 6 6)
do
java -jar duckwars.jar -sim maps/$l.txt -mn results/test \
-ts 600 \
-c "python ../AB.py" \
-c "python ../AfrankBotV01.py" \
-c "java -jar SpawnBot.jar" \
-c "java -jar SpawnBot.jar" \
-show 
done


exit 0

# end


#-c "java -jar RndBot.jar" \
