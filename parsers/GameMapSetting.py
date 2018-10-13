import os.path


class ConfigNotExists(Exception):
    pass


class GameMapSetting:

    @staticmethod
    def get_game_map_config(name):
        if not os.path.exists("./maps/" + name.lower()):
            raise ConfigNotExists('Map not exist')
