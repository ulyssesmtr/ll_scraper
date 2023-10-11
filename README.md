# Linked List and Web Scraper

## Setup
Run the following command at the project root folder to build the images and start the containers:
```
docker-compose -f docker-compose-local.yml up -d --build
```
If sucessful, two containers should be up and running, one for the Linked List application, and
another for whe Web Scraper.

## Usage

### Linked list
In order to access the Linked List container bash terminal, run the following command:
```
docker exec -it ll_scraper_linked_list_1 bash
```
Once inside the container, run the python file to check that all tests are passing:
```
python linked_list.py 
```

### Web Scraper
In order to access the Web Scraper container bash terminal, run the following command:
```
docker exec -it ll_scraper_scraper_1 bash
```
Once inside the container, run the python file passing an ICAO code as an argument
to see all the data related to that location:

```
python aisweb_scraping.py SBMT
```

If an invalid ICAO code is passed as the argument the script will return
an appropriate message.



