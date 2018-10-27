import os.path
import json
import jsonschema
from helpers.file_helper import FileHelper

class ConfigNotExists(Exception):
    pass

class InvalidSource(Exception):
    pass


class GameMapSetting:

    def __init__(self, name):
        self.name = name
        self.path = "../maps/" + self.name.lower()+'.json'
        self.schema = {
            "required": ["continents"],
            "type": "object",
            "continents": {
                "required": ["name"]},
        };

    def load_game_map_json(self):
        self.__check_if_config_exist()
        return self.__read_content_config_file()

    def check_game_map_json(self, json):
        if self.__validate_json(json):
            raise InvalidSource('Source is not valid')

    def __validate_json(self, json_document):
        try:
            datum = json.loads(json_document)
            jsonschema.validate(datum, self.schema)
        except jsonschema.exceptions.ValidationError as e:
            return True
        return False

    def __check_if_config_exist(self):
        if not os.path.exists(self.path):
            raise ConfigNotExists('Map not exist')

    def __read_content_config_file(self):
        json_data = FileHelper.read_data_from_file(self.path)
        return self.__create_map(json.loads(json_data))

    def __create_map(self,json):
        print(json)
        pass