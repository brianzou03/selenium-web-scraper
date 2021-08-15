# Changing Room Data Engineering Coding Challenge
# Code written by Brian Zou for usage on PC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yaml
import psycopg2


class Scraper():

    def __init__(self):
        with open("config.yml", "r") as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        for section in self.cfg:
            print(section)

        self.connect_db()

        options = Options()
        options.headless = True

        options.add_argument("--window-size=" + self.cfg["display"]["window_size"])

        DRIVER_PATH = self.cfg["driver"]["driver_path"]

        self.driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        self.driver.get(self.cfg["site"]["url"])

        self.root_element = self.driver.find_element_by_id("search-result-items")

    def connect_db(self):
        self.connection = psycopg2.connect(
            host=self.cfg["db"]["host"],
            port=self.cfg["db"]["port"],
            user=self.cfg["db"]["user"],
            password=self.cfg["db"]["password"],
            database=self.cfg["db"]["database"])

        self.cursor = self.connection.cursor()

    def enrich_element(self, element):
        self.driver.get(element["url"])
        my_price = self.driver.find_element_by_class_name("price-standard")
        my_color = self.driver.find_element_by_class_name("rwd-swatch-value")
        my_review_score = self.driver.find_element_by_class_name("sr-only")
        enriched_element = {"price": my_price.text,
                            "color": my_color.text[7:],
                            "review_score": my_review_score.text[:3]}
        return enriched_element


    def get_price(self, product):
        return product.find_element_by_class_name("price-standard")

    def get_name(self, name_link):
        return name_link.get_attribute("title")

    def get_link(self, name_link):
        return name_link.get_attribute("href")

    def find_element(self):
        total_products = 0
        if self.root_element:
            products = self.root_element.find_elements_by_tag_name("li")
            product_elements = []
            for product in products:
                price = self.get_price(product)
                name_link = product.find_element_by_class_name("name-link")
                name = self.get_name(name_link)
                link = self.get_link(name_link)
                # print(name, price.text, link)

                product_elements.append({"name": name,
                                         "price": price.text,
                                         "url": link})
                total_products += 1

            for element in product_elements:
                enriched_element = self.enrich_element(element)
                print(enriched_element)

                """
                self.cursor.execute('INSERT INTO products (name, price, link) VALUES ( %s, %s, %s)',
                                    (name, price.text, link))
                self.connection.commit()
                """
        return total_products


    def __del__(self):
        if self.driver:
            self.driver.quit()


scraper = Scraper()
scraper.find_element()

del scraper

