from Player import Player

class TooManyPlayersException(Exception):
    pass

class ColorAlreadyUsed(Exception):
    pass

class Risk:

    def __init__(self):
        self.players = []

    def addplayer(self, name, color, typeofplayer):
        if self.__checkfortoomanyplayers():
            self.players.append(Player(name, color, typeofplayer))
        else:
            raise TooManyPlayersException('Too many players')

    def getplayers(self):
        return self.players

    def __checkfortoomanyplayers(self):
        return len(self.players) < 6

