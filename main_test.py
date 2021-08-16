import unittest
from main import Scraper


class ScraperUnittest(unittest.TestCase):
    def setUp(self):
        # Maximum products to test set to 3
        self.scraper = Scraper(max_products=3)

    def test_scraping(self):
        total_products = self.scraper.find_element()
        # Assert returns an OK on the test if 0 < products <= 3
        assert (0 < total_products <= 3)
