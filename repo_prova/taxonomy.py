import logging

logging.basicConfig(level=logging.INFO)


class Taxonomy:
    """
    A class to represent a biological taxonomy.

    Taxonomy is the science of naming, defining and classifying groups of biological organisms on the basis of shared characteristics. Organisms are grouped together into taxa and these groups are given a taxonomic rank; groups of a given rank can be aggregated to form a more inclusive group of higher rank, thus creating a taxonomic hierarchy.
    """

    def __init__(self, kingdom:str, clade:str, order:str, family:str, genus:str, species:str):
        """
        Initialize Taxonomy with kingdom, clade, order, family, genus, species.

        :param kingdom: The kingdom of the organism. (str)
        :param clade: The clade of the organism. (str)
        :param order: The order of the organism. (str)
        :param family: The family of the organism. (str)
        :param genus: The genus of the organism. (str)
        :param species: The species of the organism. (str)
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

