# Python Web Scraper for https://pacsun.com

The web scraper project is a Python Selenium application which allows a user
to scrape the men's shirts section - https://www.pacsun.com/mens/shirts/ -
of the Pacsun clothing website. The user can view the product name, price,
color, rating, link, and sku via a query to the API. 

## Web Driver
...

## Architecture

The Python Selenium WebDriver is the backbone of the project, allowing a programmer
to navigate web pages and gather data from the HTML in an intuitive manner.

...

### Chain of Events
Selenium Web Driver (uses yaml configs, then hits link) 
--> https://www.pacsun.com/mens/shirts/ (connects to) 
--> Compose PostGreSQL database (finds elements via) -->
provided root element (accesses) --> name and link, adding both to database 
(using the product link to enrich data via) --> 
price, color, rating, and sku elements (then commits the results)
to the PostGreSQL database

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have Python 3.8 installed
* ...

### IDE Configuration

```
...
```

### Run in PyCharm

To run the project in the PyCharm IDE, ensure that your yaml file is configured
to your computer. The WebDriver should be set to the appropriate web browser, and 
may need to be installed if you are not using a PC.

Data results can be viewed in a legible table via the TablePlus application,
found at https://tableplus.com/. Changing the database type to PostGreSQL and
respective fields (found in the yaml file and crt file) will allow a user to
scrape and view the data output.

## Compose PostGreSQL Database
...

## Supported API Endpoints
...

## Unit Test
The unittest is found in the main_test.py file, and certifies that the scraper is
able to add the product name, price, color, rating, link, and sku values to the
PostGreSQL database.

## Integrations
* Python Selenium

## Development Expansion
The scraper can be expanded to scrape the entirety of the Pacsun website...

## Known Issues
...

## Technology Stack
* Java 11
...

## Contacts
If you have any questions regarding this project, please locate me at:
* brianzou03@gmail.com
* https://github.com/brianzou03
* https://www.linkedin.com/in/brian-zou-8bbab4203/

