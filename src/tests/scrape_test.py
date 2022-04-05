import unittest
from index import Scrape

class TestScrape(unittest.TestCase):
    def test_loading_website(self):
        self.load_website(self, "https://unicafe.fi/sv/restaurants/exactum/")
	self.assertTrue(self.page != "")

    def test_searching_webiste(self):
        self.load_website(self, "https://unicafe.fi/sv/restaurants/exactum/")
        self.assertTrue(self.search_for_ingredient("Rypsiöljy") > 0)
