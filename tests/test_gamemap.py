import unittest
from factories.GameMapFactory import GameMapFactory, GameMapNotExists, InvalidSource
from parsers.GameMapSetting import GameMapSetting


class GameMapTest(unittest.TestCase):

    def test_check_if_map_not_exist(self):
        with self.assertRaises(GameMapNotExists):
            self.game_map = GameMapFactory.load_game_map("not_existing_map")

    def test_check_if_source_is_invalid(self):
        json = '{"name": "invalid formatted map", "countries": {"name": "The Netherlands"}}'

        with self.assertRaises(InvalidSource):
            game_map_settings = GameMapSetting('default')
            self.game_map = game_map_settings.create_map(json)

    def test_check_if_source_is_valid(self):
        json = '{"name": "valid formatted map", "continents": {"name": "Europe"}}'
        game_map_settings = GameMapSetting('default')
        self.game_map = game_map_settings.create_map(json)


if __name__ == '__main__':
    unittest.main()