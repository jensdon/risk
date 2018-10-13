import unittest
from Risk import Risk, TooManyPlayersException, ColorAlreadyUsed, NotEnoughPlayers


class RiskTest(unittest.TestCase):

    def setUp(self):
        self.newGame = Risk()

    def generate_random_players(self, amount):
        for color in range(amount):
            self.newGame.add_player("Player", str(color), True);

    def get_mission(self):
        return

    def start_an_game(self, amount_of_players):
        self.setUp()
        self.generate_random_players(amount_of_players)
        self.newGame.start_game()

    def test_add_player(self):
        self.generate_random_players(1);
        get_player_count = len(self.newGame.get_players())
        self.assertEqual(1, get_player_count)

    def test_add_to_much_players(self):
        self.generate_random_players(6);
        with self.assertRaises(TooManyPlayersException):
            self.generate_random_players(1);

    def test_add_players_with_the_same_color(self):
        self.generate_random_players(1);
        with self.assertRaises(ColorAlreadyUsed):
            self.generate_random_players(1);

    def test_if_there_are_not_enough_players_to_start(self):
        with self.assertRaises(NotEnoughPlayers):
            self.newGame.start_game()

    def test_check_if_the_right_amount_of_armies_are_divided_to_the_players(self):
        armies = [[3, 35], [4, 30], [5, 25], [6, 20]];
        for army in armies:
            self.start_an_game(army[0])
            self.assertEqual(len(self.newGame.get_players()[0].get_armies()), army[1])

    def test_give_missions_to_players(self):
        self.start_an_game(3)
        for player in self.newGame.get_players():
            self.assertIsNotNone(player.get_mission())


if __name__ == '__main__':
    unittest.main()
