import os.path
import json
import jsonschema

class ConfigNotExists(Exception):
    pass

class InvalidSource(Exception):
    pass


class GameMapSetting:

    def __init__(self, name):
        self.name = name
        self.path = "./maps/" + self.name.lower()

    def load_game_map(self):
        self.__check_if_config_exist()
        return self.__read_content_config_file()

    def create_map(self, json):
        if self.__validate_json(json):
            raise InvalidSource('Source is not valid')

    def __validate_json(self, json_document):
        schema = {
            "required": ["continents"],
            "type": "object",
            "continents": {
                "required": ["name"]},
        }

        try:
            datum = json.loads(json_document)
            jsonschema.validate(datum, schema)
        except jsonschema.exceptions.ValidationError as e:
            return True
        except json.decoder.JSONDecodeError as e:
            return False

    def __check_if_config_exist(self):
        if not os.path.exists(self.path):
            raise ConfigNotExists('Map not exist')

    def __read_content_config_file(self):
        json_data = open(self.path).read()
        return self.create_map(json.loads(json_data))