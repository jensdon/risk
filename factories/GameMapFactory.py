from parsers.GameMapSetting import GameMapSetting, ConfigNotExists, InvalidSource
from entities.GameMap import GameMap
from entities.Continent import Continent

class GameMapNotExists(Exception):
    pass


class GameMapFactory:

    @staticmethod
    def load_game_map(name):
        game_map_settings = GameMapSetting(name)
        try:
            game_map_config_dict = game_map_settings.load_game_map_json()
            continents = GameMapFactory.__generate_continents(game_map_config_dict)
            return GameMap(game_map_config_dict['name'], continents)

        except ConfigNotExists:
            raise GameMapNotExists('Map not exist')
        except InvalidSource:
            raise InvalidSource('Invalid source')

    @staticmethod
    def __generate_continents(game_map_config_dict):
        continents = []

        for continent_dict in game_map_config_dict['continents']:
            continents.append(
                Continent(
                    continent_dict['id'],
                    continent_dict['name'],
                    continent_dict['extra_armies']
                )
            )

        return continents
