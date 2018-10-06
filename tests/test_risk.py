import unittest
import Risk


class RiskTest(unittest.TestCase):

    def setUp(self):
        self.newGame = Risk()

    def addPlayer(self):
        self.newGame.addPlayer("PlayerOne", "blue", true);
        getPlayerCount = len(self.newGame.getPlayers());
        self.assertEqual(1, getPlayerCount, "Player is not found in game.")