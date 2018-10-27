from parsers.GameMapSetting import GameMapSetting, ConfigNotExists, InvalidSource
from entities.GameMap import GameMap
from entities.Continent import Continent
from entities.Territory import Territory

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
                    continent_dict['extra_armies'],
                    GameMapFactory.__generate_territories(continent_dict['territories'])
                )
            )

        return continents

    @staticmethod
    def __generate_territories(game_map_config_dict_territories):

        territories = []

        for territory_dict in game_map_config_dict_territories:
            territories.append(
                Territory(
                    territory_dict['id'],
                    territory_dict['name']
                )
            )

        for index, territory_dict in enumerate(game_map_config_dict_territories):
            relations = []
            if territory_dict.get('relations') is not None:
                for relation_dict in territory_dict.get('relations'):
                    for territory in territories:
                        if territory.get_id() == relation_dict:
                            relations.append(territory)

                territories[index].add_related_territories(relations)

        return territories
