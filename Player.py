from Army import Army

class Player:
    def __init__(self, name, color, typeofplayer):
        self.name = name
        self.color = color
        self.typeofplayer = typeofplayer
        self.armies = [];
        self.mission = None

    def getcolor(self):
        return self.color

    def givearmies(self, amount):
        for armie in range(amount):
            self.armies.append(Army());

    def getarmies(self):
        return self.armies

    def getmission(self):
        return self.mission
