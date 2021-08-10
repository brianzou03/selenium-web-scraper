# Changing Room Data Engineering Coding Challenge
# Code written by Brian Zou

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


if root_element:
    products = root_element.find_elements_by_tag_name("li")
    for product in products:
        price = product.find_element_by_class_name("price-standard")
        # promo_price = product.find_element_by_class_name("price-promo")
        # print(product.text)
        print(price.text)
        # print(promo_price.text)


driver.quit()
