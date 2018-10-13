import unittest
from GameMapFactory import GameMapFactory, MapNotExists


class GameMapTest(unittest.TestCase):

    def test_check_if_map_not_exist(self):
        with self.assertRaises(MapNotExists):
            self.game_map = GameMapFactory.find_game_map("not_existing_map")


if __name__ == '__main__':
    unittest.main()