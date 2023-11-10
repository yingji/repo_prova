class Taxonomy:

    def __init__(kingdom:str, clade:str, order:str, family:str, genus:str, species:str):
        self.kingdom = kingdom
        self.clade = clade
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species
        self.variety = {}
        self.breeds = {}
    
    def add_breed(new_breed:str, description:str=None):
        self.breeds[new_breed] = description
    
    def list_breeds():
        if len(self.breeds)==0:
            print(f'{self.genus} {self.species} doesn't have any breed')
        for b, d in self.breeds.items():
            print(b, d)
        return self.breeds
        