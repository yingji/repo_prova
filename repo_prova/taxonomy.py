import logging

logging.basicConfig(level=logging.INFO)


class Taxonomy:
    """
    A class to represent a biological taxonomy.
    """

    def __init__(self, kingdom:str, clade:str, order:str, family:str, genus:str, species:str):
        """
        Initialize Taxonomy with kingdom, clade, order, family, genus, species.
        """
        self.kingdom = kingdom
        self.clade = clade
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species
        self.variety = {}
        self.breeds = {}
        logging.info(f'Taxonomy for {self.genus} {self.species} created.')
    
    def add_breed(self, new_breed:str, description:str=None):
        """
        Add a new breed to the taxonomy.
        """
        self.breeds[new_breed] = description
        logging.info(f'Breed {new_breed} added to {self.genus} {self.species}.')
    
    def list_breeds(self):
        """
        List all breeds in the taxonomy.
        """
        logging.info(f'Listing breeds for {self.genus} {self.species}.')
        
        if len(self.breeds)==0:
            print(f"{self.genus} {self.species} doesn't have any breed")
        
        for b, d in self.breeds.items():
            print(b, d)
        return self.breeds