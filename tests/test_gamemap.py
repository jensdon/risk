import unittest
from factories.GameMapFactory import GameMapFactory, GameMapNotExists
from entities.GameMap import GameMap


class GameMapTest(unittest.TestCase):

    def test_check_if_map_not_exist(self):
        with self.assertRaises(GameMapNotExists):
            self.game_map = GameMapFactory.make_game_map("not_existing_map")

    def test_check_if_game_map_created(self):
        game_map = GameMapFactory.make_game_map("default")
        self.assertIsInstance(game_map, GameMap)

if __name__ == '__main__':
    unittest.main()