# Python Web Scraper for https://pacsun.com

The web scraper is a Python Selenium application which allows a user
to scrape the men's shirts section - https://www.pacsun.com/mens/shirts/ -
of the Pacsun clothing website. The user can view the product name, price,
color, rating, link, and sku via a query to the API. 

## Web Driver
The scraper was designed using a PC and thus by default has the chromedriver.exe
in place as the driver path. On Mac, the driver path should be ./chromedriver -
an installation of the proper driver path to the project will be necessary on
non-Windows OS.

## Architecture

The Python Selenium WebDriver is the backbone of the project, allowing a programmer
to navigate web pages and gather data from the HTML in an intuitive manner.

### How it Works
Selenium Web Driver (uses yaml configs, then hits link) 
--> https://www.pacsun.com/mens/shirts/ (connects to) 
--> Compose PostGreSQL database (finds elements via) -->
provided root element (accesses) --> name and link, adding both to database 
(using the product link to enrich data via) --> 
price, color, rating, and sku elements (then commits the results)
to the PostGreSQL database. (Using localhost to query) -->
hits the API and returns the respective values from the
database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python 3 is installed
* Selenium WebDriver and Options are imported
* Yaml is imported
* Psycopg2 is imported
* Flask is imported
* The config.yml, SSL_certificate, main.py, server.py, main_test, and create_db files are present.


### Steps to run in PyCharm

 1. Check the project prerequisites
 2. Make sure that your yaml configurations are correct for your machine and have the correct driver_path and sslrootcert path
 3. Run create_db.py. This clears any pre-existing products, and creates a new table.
 4. Run main.py. Note that this may take several minutes to scrape.
 5. Run server.py. Now you can hit the URL, API Query instructions are below.


## Compose PostGreSQL Database
The Compose PostGreSQL Database stores scraped data into a table called products.
The table columns are name, color, rating, price, and link, in respective order. 
The primary table key is an integer column.

## API Query
In order to receive information from the Compose PostGreSQL Database, run the
server.py file, and enter the link below:

```
http://localhost:8082/search/
```

Following the link, enter a number that is within range of the database id keys.
The current id key total is roughly 24, so 1-24 will return the record in JSON
format.

In order to search for all entries, entering the link below will do such:
```
http://localhost:8082/search_all
```

## Unit Test
The unittest is found in the main_test.py file, and certifies that the scraper is
functional by testing a small batch of data. The unit test does not save to the 
database.

## Development Expansion
The scraper can be expanded to scrape the entirety of the Pacsun website.
This would take time, multiple virtual machines, and expansion of the
scraper program. My approach of this would be to divide the Pacsun website
into portions. Each category (men, women, etc.) would serve as the base,
and the respective types of clothing (shirts, pants, etc.) could be scraped
by an individual virtual machine.

## Known Issues
The current limitation of the project is not only the scope, but the amount of
information that is gathered. The project has expansion potential, as
mentioned above. The information that is gathered currently could end up
as duplicates in the database if the main is ran without first clearing the
database itself due to a lack of unique ID/sku for each products. This is
mainly due to time constraints, as the sku is present but would need more
research in executing JavaScript under Python Selenium's WebDriver, as the
sku provided in the HTML returns an empty value, likely due to the website's
dynamic aspects. 

## Technology Stack
* Python 3
* Selenium
* PostGreSQL
* Flask

## Contacts
If you have any questions regarding this project, please locate me at:
* brianzou03@gmail.com
* https://github.com/brianzou03
* https://www.linkedin.com/in/brian-zou-8bbab4203/