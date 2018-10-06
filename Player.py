from Army import Army

class Player:
    def __init__(self, name, color, typeofplayer):
        self.name = name
        self.color = color
        self.typeofplayer = typeofplayer
        self.armies = [];

    def getcolor(self):
        return self.color

    def givearmies(self, amount):
        for armie in range(amount):
            self.armies.append(Army());

    def getarmies(self):
        return self.armies


