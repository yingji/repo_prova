import unittest
from repo_prova.taxonomy import Taxonomy

class TestTaxonomy(unittest.TestCase):

    def setUp(self):
        self.taxonomy = Taxonomy('Animalia', 'Chordata', 'Mammalia', 'Canidae', 'Canis', 'lupus')

    def test_add_breed(self):
        self.taxonomy.add_breed('labrador', 'A breed of retriever')
        self.assertEqual(self.taxonomy.breeds['labrador'], 'A breed of retriever')

    def test_list_breeds(self):
        self.taxonomy.add_breed('labrador', 'A breed of retriever')
        self.taxonomy.add_breed('bulldog', 'A breed of muscular dog')
        breeds = self.taxonomy.list_breeds()
        self.assertEqual(len(breeds), 2)
        self.assertEqual(breeds['labrador'], 'A breed of retriever')
        self.assertEqual(breeds['bulldog'], 'A breed of muscular dog')

if __name__ == '__main__':
    unittest.main()