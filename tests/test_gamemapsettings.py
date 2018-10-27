import unittest
from parsers.GameMapSetting import GameMapSetting,InvalidSource


class GameMapSettingsTest(unittest.TestCase):

    def test_check_if_source_is_invalid(self):
        json = '{"name": "invalid formatted map", "countries": {"name": "The Netherlands"}}'

        with self.assertRaises(InvalidSource):
            game_map_settings = GameMapSetting('default')
            self.game_map = game_map_settings.get_game_map_json(json)

    def test_check_if_source_is_valid(self):
        json = '{"name": "valid formatted map", "continents": {"name": "Europe"}}'
        game_map_settings = GameMapSetting('default')
        self.game_map = game_map_settings.get_game_map_json(json)

    def test_check_if_default_map_is_valid(self):
        game_map_settings = GameMapSetting('default')
        self.game_map = game_map_settings.load_game_map_json()


if __name__ == '__main__':
    unittest.main()