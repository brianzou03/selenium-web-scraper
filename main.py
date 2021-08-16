# Changing Room Data Engineering Coding Challenge
# Code written by Brian Zou for usage on PC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yaml
import psycopg2


class Scraper:

    def __init__(self, save_to_database=None, max_products=-1):
        # Opens yaml file and loads configurations
        self.save_to_database = save_to_database
        self.max_products = max_products
        with open("config.yml", "r") as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        self.connect_db()

        options = Options()
        options.headless = True

        options.add_argument("--window-size=" + self.cfg["display"]["window_size"])

        DRIVER_PATH = self.cfg["driver"]["driver_path"]

        self.driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        self.driver.get(self.cfg["site"]["url"])

        # Root element allows for a search for individual products under the "li" tag
        self.root_element = self.driver.find_element_by_id("search-result-items")

    # Connects to database using yaml configurations
    def connect_db(self):
        self.connection = psycopg2.connect(
            host=self.cfg["db"]["host"],
            port=self.cfg["db"]["port"],
            user=self.cfg["db"]["user"],
            password=self.cfg["db"]["password"],
            database=self.cfg["db"]["database"],
            sslmode=self.cfg["db"]["sslmode"],
            sslrootcert=self.cfg["db"]["sslrootcert"])

        self.cursor = self.connection.cursor()

    # Finds price, color, and rating through the provided product URL
    def enrich_element(self, element):
        try:
            self.driver.get(element["url"])
            my_price = self.driver.find_element_by_class_name("price-standard")
            my_color = self.driver.find_element_by_class_name("rwd-swatch-value")
            my_rating = self.driver.find_element_by_class_name("sr-only")

            enriched_element = {"color": my_color.text[7:],
                                "rating": my_rating.text[:3],
                                "price": my_price.text
                                }
        except:
            print("Can't scrape url", element["url"])
            enriched_element = None

        return enriched_element

    # Gets the name via title attribute in HTML
    def get_name(self, name_link):
        return name_link.get_attribute("title")

    # Gets the link via the href attribute in HTML
    def get_link(self, name_link):
        return name_link.get_attribute("href")

    # Locates elements from the shirt page, gathers enriched information via links, saves to database
    def find_element(self):
        total_products = 0
        if self.root_element:
            products = self.root_element.find_elements_by_tag_name("li")
            product_elements = []
            for product in products:
                try:
                    name_link = product.find_element_by_class_name("name-link")
                    name = self.get_name(name_link)
                    link = self.get_link(name_link)
                    # Appends name and URL to product_elements list
                    product_elements.append({"name": name,
                                             "url": link
                                             })
                except:
                    print("Can't scrape ", str(total_products) + "s")
                # Total product counter for unittest
                total_products += 1
                if 0 < self.max_products <= total_products:
                    break
            total_products = 0
            # Prints enriched elements to console for development purposes
            for element in product_elements:
                enriched_element = self.enrich_element(element)
                print(enriched_element)
                if self.save_to_database == 'require' and enriched_element is not None:
                    try:
                        # Inserts the data into the proper fields in the PostGreSQL database
                        self.cursor.execute('INSERT INTO products (name, color, rating, price, link) '
                                            'VALUES ( %s, %s, %s, %s, %s)',
                                            (element["name"],
                                             enriched_element["color"],
                                             enriched_element["rating"],
                                             enriched_element["price"],
                                             element["url"]))
                        self.connection.commit()
                    except:
                        print("Failed to save to database " + str(enriched_element))
                # Total product counter for enriched data
                total_products += 1
                if 0 < self.max_products <= total_products:
                    return total_products
        return total_products

    def __del__(self):
        if self.driver:
            self.driver.quit()


# Prevents the unittest from sending values to the database
if __name__ == '__main__':
    scraper = Scraper(
        save_to_database='require'
    )
    scraper.find_element()

    del scraper
