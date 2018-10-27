class GameMap:
    def __init__(self, name,continents):
        self.name = name
        self.continents = continents

    def get_continents(self):
        return self.continents

    def get_territory_by_id(self,territory_id):
        for continent in self.continents:
            for territory in continent.get_territories():
                if territory.get_id() == territory_id:
                    return territory
