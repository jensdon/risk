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
        self.assertEqual(1, getplayercount, "Player is not found in game.")

    def test_addtomuchplayers(self):
        self.generateRandomplayers(6);
        with self.assertRaises(TooManyPlayersException):
          self.newGame.addplayer("PlayerOne", "blue", True)

    def test_addplayerswiththesamecolor(self):
        self.newGame.addplayer("Player", "blue", True)
        with self.assertRaises(ColorAlreadyUsed):
          self.newGame.addplayer("PlayerOne", "blue", True)

    def test_iftherearenotenoughplayerstostart(self):
        with self.assertRaises(NotEnoughPlayers):
          self.newGame.startgame()


if __name__ == '__main__':
    unittest.main()
