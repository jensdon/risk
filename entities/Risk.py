import numpy as np
from random import shuffle
from entities.Player import Player
from entities.Missions import Missions
from entities.GameMap import GameMap
from factories.GameMapFactory import GameMapFactory


class TooManyPlayersException(Exception):
    pass

class ColorAlreadyUsed(Exception):
    pass

class NotEnoughPlayers(Exception):
    pass

class Risk:

    def __init__(self):
        self.players = []
        self.missions = Missions()
        self.game_map = None

    def add_player(self, name, color, type_of_player):
        self.__check_for_too_many_players()
        self.__check_if_color_is_already_been_used(color)
        self.players.append(Player(name, color, type_of_player))

    def get_players(self):
        return self.players

    def start_game(self):
        self.__check_if_there_are_enough_players()
        self.__divide_armies_to_all_players()
        self.__divide_missions_for_all_players()
        self.game_map = GameMapFactory.load_game_map("default")
        self.__divide_territories_for_all_players()

    def __divide_territories_for_all_players(self):
        territories = self.game_map.get_territories()
        shuffle(territories)
        divided_territories = np.array_split(territories, len(self.players))
        shuffle(divided_territories)
        for index, player in enumerate(self.players):
            player.receive_territories(divided_territories[index])

    def __divide_missions_for_all_players(self):
        for player in self.players:
            player.receive_mission(self.missions.get_mission())

    def __give_all_players_amount_of_armies(self, amount):
        for player in self.players:
            player.receive_armies(amount)

    def __divide_armies_to_all_players(self):
        self.__give_all_players_amount_of_armies((10 - len(self.players)) * 5)

    def __check_if_there_are_enough_players(self):
        if len(self.players) < 2:
            raise NotEnoughPlayers('Not enough players')

    def __check_for_too_many_players(self):
        if len(self.players) > 5:
            raise TooManyPlayersException('Too many players')

    def __check_if_color_is_already_been_used(self,color):
        for player in self.players:
            if player.get_color() == color:
                raise ColorAlreadyUsed('Color already in use')

