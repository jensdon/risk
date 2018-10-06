import unittest
from Risk import Risk


class RiskTest(unittest.TestCase):

    def setUp(self):
        self.newGame = Risk()

    def test_addplayer(self):
        self.newGame.addplayer("PlayerOne", "blue", True);
        getplayercount = len(self.newGame.getplayers());
        self.assertEqual(1, getplayercount, "Player is not found in game.")

    def test_addtomuchplayers(self):
        for addPlayer in range(5):
            self.newGame.addplayer("Player", "blue", True);
        self.assertRaises(Exception, self.newGame.addplayer("PlayerOne", "blue", True))


if __name__ == '__main__':
    unittest.main()
