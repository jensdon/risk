import unittest
from factories.GameMapFactory import GameMapFactory, GameMapNotExists


class GameMapTest(unittest.TestCase):

    def test_check_if_map_not_exist(self):
        with self.assertRaises(GameMapNotExists):
            self.game_map = GameMapFactory.make_game_map("not_existing_map")


if __name__ == '__main__':
    unittest.main()