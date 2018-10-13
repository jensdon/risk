import os.path

class MapNotExists(Exception):
    pass


class GameMapFactory:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_game_map(name):
        if not os.path.exists("./maps/" + name.lower()):
            raise MapNotExists('Map not exist')


