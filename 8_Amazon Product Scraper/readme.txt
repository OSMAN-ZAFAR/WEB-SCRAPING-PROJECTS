=> Amazon Products Scraper

This project is a simple "web scraping script" built with Python.  
It scrapes **Oppo phone product details** (links, names, prices, availability, and ratings) from [Amazon](https://www.amazon.com) and saves the data into a CSV file.

=>Features
-> Extracts "product names/details"  
-> Extracts "product prices"  
-> Extracts "availability status"  
-> Extracts "customer ratings"  
-> Extracts "direct product links"  
-> Stores data in a structured "CSV file" (`Amazon Products.csv`)  

=>Technologies Used
-> "Python"  
-> "Requests" → For fetching the webpage  
-> "BeautifulSoup" → For parsing HTML content  
-> "itertools (zip_longest)" → For handling unequal list lengths  
-> "Pandas" → For creating and saving data in CSV format  

=>How to Run
-> Clone this repository or copy the script.  
-> Install the required libraries (if not installed yet):  
```bash
->pip install requests pandas beautifulsoup4 lxml
->python scraper.py
