class Player:
    def __init__(self, name, color, typeofplayer):
        self.name = name
        self.color = color
        self.typeofplayer = typeofplayer

    def getcolor(self):
        return self.color