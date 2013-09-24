#!/usr/bin/python
#
# play - play all possible variations, thread it ;)
# the result store in results/gameXX/...
#
import os
from subprocess import *

gamer1 ='"java -jar SpawnBot.jar"'
gamer2 ='"java -jar ModeBot.jar"'
gamer3 ='"java -jar RndBot.jar"'
gamer3 ='"java -jar AfrankBot1.0.jar"'
gamer4 ='"php phpBot.php"'

me='python ../AfrankBot1.py'

maps = ['maps/%02d.txt'%x for x in range(1,36)]

cnt=0
for m in maps:
    print "round %d"%cnt
    path='results/game%02d'%cnt
    print path
    try:
        os.removedirs(path)
    except OSError:
        pass
    os.mkdir(path)
    cmd=['java', '-jar', 'duckwars.jar', '-sim', m, '-mn', path+'/test', '-ts', '500']
    cmd.append('-c')
    cmd.append(gamer1)
    cmd.append('-c')
    cmd.append(gamer2)
    process = Popen(cmd, stderr=PIPE)
    process.wait()
    cnt=cnt+1



