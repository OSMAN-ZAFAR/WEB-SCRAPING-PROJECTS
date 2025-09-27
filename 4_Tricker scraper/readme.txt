=>Stock Market 52-Week High Scraper

This project is a simple "web scraping script" built with Python.  
It scrapes "stock market data" (company names, current prices, and day high prices) from [Finology Ticker](https://ticker.finology.in/market/52-week-high) and saves the data into a CSV file.

=>Features
-> Extracts "company names"  
-> Extracts "current prices"  
-> Extracts "day high prices"  
-> Stores data in a structured "CSV file" (`04_Tricker Details.csv`)  

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
