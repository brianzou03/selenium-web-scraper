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
print(driver.page_source)


driver.quit()