from Army import Army


class Player:
    def __init__(self, name, color, type_of_player):
        self.name = name
        self.color = color
        self.type_of_player = type_of_player
        self.armies = []
        self.mission = None

    def get_color(self):
        return self.color

    def give_armies(self, amount):
        for army in range(amount):
            self.armies.append(Army())

    def get_armies(self):
        return self.armies

    def get_mission(self):
        return self.mission

    def receive_mission(self, mission):
        self.mission = mission
