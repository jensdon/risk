class Territory:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.related_territories = []

    def get_id(self):
        return self.id

    def get_related_territories(self):
        return self.related_territories