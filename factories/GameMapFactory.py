from parsers.GameMapSetting import GameMapSetting, ConfigNotExists, InvalidSource


class GameMapNotExists(Exception):
    pass


class GameMapFactory:

    @staticmethod
    def load_game_map(name):
        game_map_settings = GameMapSetting(name)
        try:
            return game_map_settings.load_game_map_json()
        except ConfigNotExists:
            raise GameMapNotExists('Map not exist')
        except InvalidSource:
            raise InvalidSource('Invalid source')
