import unittest
from main import Scraper


class ScraperUnittest(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_scraping(self):
        total_products = self.scraper.find_element()
        assert (total_products > 0)

