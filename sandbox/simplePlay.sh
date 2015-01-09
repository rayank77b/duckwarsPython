#java -jar duckwars.jar -sim maps/01.txt -mn results/test -ts 400 -c "java -jar SpawnBot.jar" -c "java -jar ModeBot.jar" -c "java -jar RndBot.jar" -c "python ../AfrankBot.py" -show
#java -jar duckwars.jar -sim maps/01.txt -mn results/test -ts 100 -c "java -jar SpawnBot.jar" -c "java -jar ModeBot.jar" -c "java -jar RndBot.jar" -show

java -jar duckwars.jar -sim maps/09.txt -mn results/test \
-ts 300 \
-c "python ../AB.py" \
-c "python ../AfrankBotV01.py" \
-c "java -jar SpawnBot.jar" \
-c "java -jar RndBot.jar" \
-show \
# end



