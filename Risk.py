from Player import Player

class TooManyPlayersException(Exception):
    pass

class ColorAlreadyUsed(Exception):
    pass

class NotEnoughPlayers(Exception):
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

    def startgame(self):
        self.__checkifthereareenoughplayers()
        self.__dividearmiestoallplayers()

    def __giveallplayersamountofarmies(self,amount):
        for player in self.players:
            player.givearmies(amount)

    def __dividearmiestoallplayers(self):
        self.__giveallplayersamountofarmies((10 - len(self.players)) * 5)

    def __checkifthereareenoughplayers(self):
        if len(self.players) < 2:
            raise NotEnoughPlayers('Not enough players')

    def __checkfortoomanyplayers(self):
        if len(self.players) > 5:
            raise TooManyPlayersException('Too many players')

    def __checkifcolorisalreadybeenused(self,color):
        for player in self.players:
            if player.getcolor() == color:
                raise ColorAlreadyUsed('Color already in use')

