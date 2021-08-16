# Python Web Scraper for https://pacsun.com

The web scraper project is a Python Selenium application which allows a user
to scrape the men's shirts section - https://www.pacsun.com/mens/shirts/ -
of the Pacsun clothing website. The user can view the product name, price,
color, rating, link, and sku via a query to the API. 

## Web Driver
The scraper was designed using a PC and thus by default has the chromedriver.exe
in place as the driver path. On Mac, the driver path should be ./chromedriver -
an installation of the proper driver path to the project will be necessary on
non Windows OS.

## Architecture

The Python Selenium WebDriver is the backbone of the project, allowing a programmer
to navigate web pages and gather data from the HTML in an intuitive manner.

...

### How it Works
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
* Selenium WebDriver and Options are imported
* Yaml is imported
* Psycopg2 is imported
* The config.yml, SSL_certificate, main.py, and main_test files are present

### IDE Configuration

```
...
```

### Steps to run in PyCharm

#### 1
#### 2
#### 3

To run the project in the PyCharm IDE, ensure that your yaml file is configured
to your computer. The WebDriver should be set to the appropriate web browser, and 
may need to be installed if you are not using Windows.

Data results can be viewed in a legible table via the TablePlus application,
found at https://tableplus.com/. Changing the database type to PostGreSQL and
respective fields (found in the yaml file and crt file) will allow a user to
scrape and view the data output.

SSL Certificate necessary
SSL Certificate path...


## Compose PostGreSQL Database
...

## API Query
In order to receive information from the Compose PostGreSQL Database, ...

## Unit Test
The unittest is found in the main_test.py file, and certifies that the scraper is
able to add the product name, price, color, rating, link, and sku values to the
PostGreSQL database by ...

## Integrations
* Python Selenium
* ...

## Development Expansion
The scraper can be expanded to scrape the entirety of the Pacsun website.
This would take time, multiple virtual machines, and expansion of the
scraper program. My approach of this would be to divide the Pacsun website
into portions. Each category (men, women, etc.) would serve as the base,
and the respective types of clothing (shirts, pants, etc.) could be scraped
by an individual virtual machine...

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
...

## Contacts
If you have any questions regarding this project, please locate me at:
* brianzou03@gmail.com
* https://github.com/brianzou03
* https://www.linkedin.com/in/brian-zou-8bbab4203/

