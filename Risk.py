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
            if self.__checkifcolorisalreadybeenused(color) == False:
                self.players.append(Player(name, color, typeofplayer))
            else:
                raise ColorAlreadyUsed('Color already in use')
        else:
            raise TooManyPlayersException('Too many players')

    def getplayers(self):
        return self.players

    def __checkfortoomanyplayers(self):
        return len(self.players) < 6

    def __checkifcolorisalreadybeenused(self,color):
        for player in self.players:
            if player.getcolor() == color:
                return True
        return False

