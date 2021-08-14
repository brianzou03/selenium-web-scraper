# Changing Room Data Engineering Coding Challenge
# Code written by Brian Zou for usage on PC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'chromedriver.exe'

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.pacsun.com/mens/shirts/")
# print(driver.page_source)

root_element = driver.find_element_by_id("search-result-items")


class Scraper():

    def __init__(self):
        pass

    def get_price(self, product):
        return product.find_element_by_class_name("price-standard")

    def get_name(self, name_link):
        return name_link.get_attribute("title")

    def get_link(self, name_link):
        return name_link.get_attribute("href")

    def find_element(self):
        if root_element:
            products = root_element.find_elements_by_tag_name("li")
            for product in products:
                price = self.get_price(product)
                name_link = product.find_element_by_class_name("name-link")
                name = self.get_name(name_link)
                link = self.get_link(name_link)
                print(price.text)
                print(name)
                print(link)


my_obj = Scraper()
my_obj.find_element()

driver.quit()