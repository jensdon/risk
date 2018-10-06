import unittest
from Risk import Risk,TooManyPlayersException,ColorAlreadyUsed,NotEnoughPlayers

class RiskTest(unittest.TestCase):

    def setUp(self):
        self.newGame = Risk()

    def generateRandomplayers(self,amount):
        for color in range(amount):
            self.newGame.addplayer("Player", str(color), True);

    def test_addplayer(self):
        self.generateRandomplayers(1);
        getplayercount = len(self.newGame.getplayers());
        self.assertEqual(1, getplayercount)

    def test_addtomuchplayers(self):
        self.generateRandomplayers(6);
        with self.assertRaises(TooManyPlayersException):
            self.generateRandomplayers(1);

    def test_addplayerswiththesamecolor(self):
        self.generateRandomplayers(1);
        with self.assertRaises(ColorAlreadyUsed):
            self.generateRandomplayers(1);

    def test_iftherearenotenoughplayerstostart(self):
        with self.assertRaises(NotEnoughPlayers):
          self.newGame.startgame()

    def test_checkiftherightamountofamriesaredividedtotheplayers(self):
        armies = [[3,35],[4,30],[5,25],[6,20]];
        for armie in armies:
            self.setUp()
            self.generateRandomplayers(armie[0]);
            self.newGame.startgame()
            self.assertEqual(len(self.newGame.getplayers()[0].getArmies()), armie[1])


if __name__ == '__main__':
    unittest.main()
