import unittest
from Risk import Risk


class RiskTest(unittest.TestCase):

    def setUp(self):
        self.newGame = Risk()

    def test_addPlayer(self):
        self.newGame.addplayer("PlayerOne", "blue", True);
        getplayercount = len(self.newGame.getplayers());
        self.assertEqual(1, getplayercount, "Player is not found in game.")


if __name__ == '__main__':
    unittest.main()
