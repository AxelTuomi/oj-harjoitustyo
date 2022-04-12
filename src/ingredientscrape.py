import requests
from selenium import webdriver

#PATH = "/src/chromedriver"

#driver = webdriver.Chrome(PATH)

class IngredientScrape:
    def __init__(self):
        self.page = ""

    def load_website(self, URL):
        self.page = requests.get(URL)
        #driver.get(URL)
        #self.page = driver.page_source

    def search_for_ingredient(self, ingredient):
        ingredientsfound = self.page.find(ingredient)
        return ingredientsfound
