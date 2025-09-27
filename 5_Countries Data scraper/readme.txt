=>Countries by Population Scraper

This project is a simple "web scraping script" built with Python.  
It scrapes "country population data" (from a Wikipedia table of countries and dependencies by population) and saves the data into a CSV file.

=>Features
-> Extracts "table headers dynamically"  
-> Extracts "country names and population details"  
-> Collects data row by row from the Wikipedia table  
-> Stores data in a structured "CSV file" (`05_Countries Details.csv`)  

=>Technologies Used
-> "Python"  
-> "Requests" → For fetching the webpage  
-> "BeautifulSoup" → For parsing HTML content  
-> "Pandas" → For creating and saving data in CSV format  

=>How to Run
->Clone this repository or copy the script.  
->Install the required libraries (if not installed yet):  
```bash
->pip install requests pandas beautifulsoup4 lxml
->python scraper.py
