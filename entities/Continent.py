class Continent:

    def __init__(self, id,name,extra_armies,territories):
        self.id = id
        self.name = name
        self.extra_armies = extra_armies
        self.territories = territories

    def get_territories(self):
        return self.territories
