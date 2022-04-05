import requests

class Scrape:
    def __init__(self):
        self.page = ""

    def load_website(self, URL):
	self.page = requests.get(URL)

    def search_for_ingredient(self, ingredient):
        ingredientsfound = self.page.find(ingredient)
	return ingredientsfound
