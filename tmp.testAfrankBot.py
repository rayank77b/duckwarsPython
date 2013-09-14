class AfrankBotTest(unittest.TestCase):
    def test_calculateDistance(self):
        #  = Camp(id, campOwner, campMancount, campSize, posX, posY)
        c1 = Camp(0,  1, 20, 5, 1, 1)
        c2 = Camp(1,  1, 20, 5, 5, 5)
        self.failUnlessEqual(calculateDistance(c1,c2),32)
        c2 = Camp(1,  1, 20, 5, 3, 5)
        self.failUnlessEqual(calculateDistance(c1,c2),(2*2+4*4))
        c2 = Camp(1,  1, 20, 5, 35, 55)
        self.failUnlessEqual(calculateDistance(c1,c2),(34*34+54*54))

    def test_calculateDistances(self):
        camps=createCamps()
        t1 = time.time()
        distances=calculateDistances(camps)
        t2 = time.time()
        dif = (t2-t1)*1000000
        #print "%d us"%dif
        for d in distances:
            for x in d:
                if x==0:
                    print "oooo some zero",d
                    self.fail()

    def test_getMinDistance(self):
        camps=createCamps()
        distances=calculateDistances(camps)
        self.failUnlessEqual(getMinDistance(distances, 12),6329)
        self.failUnlessEqual(getMinDistance(distances, 1),16)
        self.failUnlessEqual(getMinDistance(distances, 2),2)
        self.failUnlessEqual(getNearestCamp(distances,8),5)
        self.failUnlessEqual(getNearestCamp(distances,9),6)

    def test_getNearestCamp(self):
        camps=createCamps()
        distances=calculateDistances(camps)
        self.failUnlessEqual(getNearestCamp(distances,19),12)
        self.failUnlessEqual(getNearestCamp(distances,15),12)
        self.failUnlessEqual(getNearestCamp(distances,12),15)
        self.failUnlessEqual(getNearestCamp(distances,3),2)
        self.failUnlessEqual(getNearestCamp(distances,10),18)
        self.failUnlessEqual(getNearestCamp(distances,18),10)
        self.failUnlessEqual(getNearestCamp(distances,1),2)

    def test_AfrankBot(self):
        bot = AfrankBot1()
        self.failUnlessEqual(bot.getName(),"AfrankBot1")
        gs=createGameState()
        print "Camps size: %d"%gs.getNumCamps()
        bot.doTurn(gs)

