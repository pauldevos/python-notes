# Best Practices

Config Files, e.g. `config.py`
- Strings, Integers, Booleans
- Try to stay away from having more complex objects in this file.
- Should be a text file

Logging
Pathlib
Formating Strings


A Class initializer should return an instance of that class

Factory Pattern
Dictionary: String names to class initializers 


### Web Scraping Project Structure
- scraper
    init.py
    pdf.py
    csv.py



Deciding on Instance Methods
whether you need `self.variable_name` or not 
- are they dependent upon instance creation?

Testing
Pure functions vs instance methods, class methods


Protocols

Scraper Protocol class

class Scraper(Protocol):
    def scrape(self, search_text: str) -> scrape_result


Logging




