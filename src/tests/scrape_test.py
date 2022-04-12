import unittest
from ingredientscrape import IngredientScrape

class TestIngredientScrape(unittest.TestCase):
    def setUp(self):
        self.ingredientscrapeinstance = IngredientScrape()

    def test_loading_website(self):
        self.ingredientscrapeinstance.load_website("https://unicafe.fi/sv/restaurants/exactum/")
        self.assertTrue(self.ingredientscrapeinstance.page != "")

    def test_searching_webiste(self):
        self.ingredientscrapeinstance.load_website("https://unicafe.fi/sv/restaurants/exactum/")
        self.assertTrue(self.ingredientscrapeinstance.search_for_ingredient("rypsiöljy") > 0)
