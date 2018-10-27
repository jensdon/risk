from parsers.GameMapSetting import GameMapSetting, ConfigNotExists, InvalidSource
from entities.GameMap import GameMap

class GameMapNotExists(Exception):
    pass


class GameMapFactory:

    @staticmethod
    def load_game_map(name):
        game_map_settings = GameMapSetting(name)
        try:
            game_map_config_dict = game_map_settings.load_game_map_json()

            return GameMap(game_map_config_dict['name'])

        except ConfigNotExists:
            raise GameMapNotExists('Map not exist')
        except InvalidSource:
            raise InvalidSource('Invalid source')