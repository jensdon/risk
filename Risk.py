from Player import Player


class Risk:

    def __init__(self):
        self.players = []

    def addplayer(self, name, color, typeofplayer):
        if self.__checkfortoomanyplayers():
            print('blaa')
            self.players.append(Player(name, color, typeofplayer))
        else:
            raise Exception('Too many players')

    def getplayers(self):
        return self.players

    def __checkfortoomanyplayers(self):
        print(len(self.players))
        return len(self.players) < 6

