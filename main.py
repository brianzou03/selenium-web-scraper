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


class PriceSearch:

    def __init__(self):
        pass

    def find_price(self):

        if root_element:
            products = root_element.find_elements_by_tag_name("li")
            for product in products:
                price = product.find_element_by_class_name("price-standard")
                # print(product.text)
                print(price.text)


my_obj = PriceSearch()
my_obj.find_price()

driver.quit()

