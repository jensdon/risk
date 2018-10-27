import unittest
from factories.GameMapFactory import GameMapFactory, GameMapNotExists
from entities.GameMap import GameMap


class GameMapTest(unittest.TestCase):

    def generate_normal_map(self):
        self.game_map = GameMapFactory.load_game_map("default")
        self.continents = self.game_map.get_continents()

    def test_check_if_map_not_exist(self):
        with self.assertRaises(GameMapNotExists):
            self.game_map = GameMapFactory.load_game_map("not_existing_map")

    def test_can_create_gamemap(self):
        self.assertTrue(type(GameMapFactory.load_game_map("default")) is GameMap)

    def test_gamemap_has_continents(self):
        self.generate_normal_map()
        self.assertTrue(len(self.continents) > 0)

    def test_gamemap_continents_have_territories(self):
        self.generate_normal_map()
        for continent in self.continents:
            self.assertTrue(len(continent.get_territories()) > 0)

    def test_gamemap_territories_relations(self):
        self.generate_normal_map()
        territory = self.game_map.get_territory_by_id(1)
        self.assertTrue(len(territory.get_related_territories()) == 3)

    def test_count_if_all_continents_are_created(self):
        self.generate_normal_map()
        self.assertTrue(len(self.game_map.get_continents()) == 6)

if __name__ == '__main__':
    unittest.main()
