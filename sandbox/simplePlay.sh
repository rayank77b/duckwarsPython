#java -jar duckwars.jar -sim maps/01.txt -mn results/test -ts 400 -c "java -jar SpawnBot.jar" -c "java -jar ModeBot.jar" -c "java -jar RndBot.jar" -c "python ../AfrankBot.py" -show
#java -jar duckwars.jar -sim maps/01.txt -mn results/test -ts 100 -c "java -jar SpawnBot.jar" -c "java -jar ModeBot.jar" -c "java -jar RndBot.jar" -show

for l in $(seq 58 60)
do
java -jar duckwars.jar -sim maps/$l.txt -mn results/test \
-ts 600 \
-c "python ../AB.py" \
-c "python ../AfrankBotV01.py" \
-c "java -jar SpawnBot.jar" \
-c "java -jar SpawnBot.jar" \
-show 
done




# end


#-c "java -jar RndBot.jar" \
