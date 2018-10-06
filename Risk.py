from Player import Player

class TooManyPlayersException(Exception):
    pass

class ColorAlreadyUsed(Exception):
    pass

class Risk:

    def __init__(self):
        self.players = []

    def addplayer(self, name, color, typeofplayer):
        self.__checkfortoomanyplayers()
        self.__checkifcolorisalreadybeenused(color)
        self.players.append(Player(name, color, typeofplayer))

    def getplayers(self):
        return self.players

    def __checkfortoomanyplayers(self):
        if len(self.players) > 5:
            raise TooManyPlayersException('Too many players')

    def __checkifcolorisalreadybeenused(self,color):
        for player in self.players:
            if player.getcolor() == color:
                raise ColorAlreadyUsed('Color already in use')

