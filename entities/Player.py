from entities.Army import Army
from entities.GameMap import GameMap

class Player:
    def __init__(self, name, color, type_of_player):
        self.name = name
        self.color = color
        self.type_of_player = type_of_player
        self.armies = []
        self.territories = []
        self.mission = None

    def get_color(self):
        return self.color

    def receive_territories(self,territories):
        self.territories = territories

    def get_territories(self):
        return self.territories

    def receive_armies(self, amount):
        for army in range(amount):
            self.armies.append(Army())

    def get_armies(self):
        return self.armies

    def get_mission(self):
        return self.mission

    def receive_mission(self, mission):
        self.mission = mission
