from Mission import Mission
import random


class Missions:
    def __init__(self):
        self.missions = [];
        self.__generate_missions();

    def get_mission(self):
        if(len(self.missions) > 0):
            random_index = self.__get_random_mission_index()
            mission = self.missions[random_index]
            self.__remove_mission_from_deck(random_index)
            return mission
        else:
            return None

    def __get_random_mission_index(self):
        return random.randrange(len(self.missions))

    def __remove_mission_from_deck(self,index):
        self.missions.pop(index)

    def __generate_missions(self):
        self.missions.append(Mission(1))
        self.missions.append(Mission(2))
        self.missions.append(Mission(3))
        self.missions.append(Mission(4))
        self.missions.append(Mission(5))
        self.missions.append(Mission(6))
        self.missions.append(Mission(7))
