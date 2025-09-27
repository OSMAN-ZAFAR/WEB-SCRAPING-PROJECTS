=>Books Data Scraper

This project is a simple "web scraping script" built with Python.  
It scrapes "book details" (title, price, and availability) from the sample website [Books to Scrape](http://books.toscrape.com/) and saves the data into a CSV file.

=>Features
-> Extracts "book titles"  
-> Extracts "book prices"  
-> Extracts "availability status"  
-> Stores data in a structured "CSV file" (`Books Details.csv`)  

=>Technologies Used
- >"Python"  
- >"Requests" → For fetching the webpage  
- >"BeautifulSoup" → For parsing HTML content  
- >"Pandas" → For creating and saving data in CSV format  

How to Run
->Clone this repository or copy the script.  
->Install the required libraries (if not installed yet):  
 ```bash
->pip install requests pandas beautifulsoup4 lxml
->python scraper.py
