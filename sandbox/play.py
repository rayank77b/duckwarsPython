#!/usr/bin/python
#
# play - play all possible variations, thread it ;)
# the result store in results/mapXX/gameXX/...
#
import os
from subprocess import *
import threading

def lock(path):
    with open(path+'/gaming.txt', 'a'):
        os.utime(path, None)

def unlock(path):
    os.remove(path+'/gaming.txt')

class Play(threading.Thread):
    def __init__(self, cnt, gamers, me):
        threading.Thread.__init__(self)
        self.cnt    = cnt
        self.gamers = gamers
        self.me     = me
    
    def get_cmd(self, maps, path, gamers):
        cmd=['java', '-jar', 'duckwars.jar', '-sim', maps, '-mn', path+'/test', '-ts', '500']
        for x in self.gamers:
            cmd.append('-c')
            cmd.append(x)
        return cmd
        
    def run(self):
        m = 'maps/%02d.txt'%self.cnt
        pathm='results/map%02d'%self.cnt
        
        # renew dir
        os.system('rm -rf %s'%pathm) 
        os.mkdir(pathm)
        
        print "round ", self.cnt
        i=0
        for gamer in self.gamers:  # we should test all game varitations
            pathg='/game%02d'%i
            os.mkdir(pathm+pathg)
            lock(pathm+pathg)
            cmd = self.get_cmd(m, pathm+pathg, [gamer, me])
            process = Popen(cmd, stderr=PIPE)
            process.wait()
            unlock(pathm+pathg)
            i=i+1

gamer1 ='"java -jar SpawnBot.jar"'
gamer2 ='"java -jar ModeBot.jar"'
gamer3 ='"java -jar RndBot.jar"'
gamer4 ='"java -jar AfrankBot1.0.jar"'
gamer5 ='"php phpBot.php"'

me='python ../AfrankBot1.py'

mapscount=35
meine_threads = [] 

for cnt in range(1,mapscount+1):
    thread = Play(cnt, [gamer1, gamer2, gamer3, gamer4, gamer5], me) 
    meine_threads.append(thread) 
    thread.start() 

for t in meine_threads: 
    t.join()
