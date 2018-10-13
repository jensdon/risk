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

    def load_game_map(self):
        path = "./maps/" + self.name.lower()
        if not os.path.exists(path):
            raise ConfigNotExists('Map not exist')
        else :
            json_data = open(path).read()
            return self.create_map(json.loads(json_data))

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
