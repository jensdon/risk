import os.path

class MapNotExists(Exception):
    pass


class GameMapFactory:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_game_map_config(name):
        if not os.path.exists("./maps/" + name.lower()):
            raise MapNotExists('Map not exist')

    @staticmethod
    def make_game_map(name):
        return GameMapFactory.get_game_map_config(name)


