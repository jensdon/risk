from Player import Player


class Risk:

    def __init__(self):
        self.players = []

    def addplayer(self, name, color, typeofplayer):
        self.players.append(Player(name, color, typeofplayer))

    def getplayers(self):
        return self.players
