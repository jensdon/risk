from Player import Player


class Risk:

    def __init__(self):
        self.players = []

    def addplayer(self, name, color, typeofplayer):
        if len(self.players) < 7:
            self.players.append(Player(name, color, typeofplayer))
        else:
            raise Exception('Too many players')

    def getplayers(self):
        return self.players
