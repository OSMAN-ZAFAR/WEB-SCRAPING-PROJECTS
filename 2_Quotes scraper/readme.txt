=>Quotes Scraper

This project is a simple "web scraping script" built with Python.  
It scrapes "quotes and their authors" from the sample website [Quotes to Scrape](http://quotes.toscrape.com/) and saves the data into a CSV file.

=>Features

->Extracts "quotes text"  
->Extracts "author names"  
->Stores data in a structured "CSV file" (`Quotions.csv`)  

=>Technologies Used

->"Python"  
->"Requests" → For fetching the webpage  
->"BeautifulSoup" → For parsing HTML content  
->"Pandas" → For creating and saving data in CSV format  


=>How to Run

->Clone this repository or copy the script.  
->Install the required libraries (if not installed yet):  

   ```bash
-> pip install requests pandas beautifulsoup4 lxml
->python scraper.py
