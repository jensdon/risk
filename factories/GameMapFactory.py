from parsers.GameMapSetting import GameMapSetting,ConfigNotExists


class GameMapNotExists(Exception):
    pass


class GameMapFactory:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def make_game_map(name):
        try:
            return GameMapSetting.get_game_map_config(name)
        except ConfigNotExists:
            raise GameMapNotExists('Map not exist')
