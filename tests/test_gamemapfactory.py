import unittest
from factories.GameMapFactory import GameMapFactory, GameMapNotExists
from entities.GameMap import GameMap


class GameMapTest(unittest.TestCase):

    def test_check_if_map_not_exist(self):
        with self.assertRaises(GameMapNotExists):
            self.game_map = GameMapFactory.load_game_map("not_existing_map")

    def test_can_create_gamemap(self):
        self.assertTrue(type(GameMapFactory.load_game_map("default")) is GameMap)


if __name__ == '__main__':
    unittest.main()