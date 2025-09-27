=>Hockey Teams Data Scraper

This project is a simple "web scraping script" built with Python.  
It scrapes "hockey team data" (team names, stats, and other details) from [Scrape This Site](https://www.scrapethissite.com/pages/forms/) and saves the data into a CSV file.

=>Features
-> Extracts "table headers dynamically"  
-> Scrapes hockey teams' details across multiple pages  
-> Collects data row by row from the table  
-> Stores data in a structured "CSV file" (`06_Team Details.csv`)  

=>Technologies Used
-> "Python"  
-> "Requests" → For fetching the webpage  
-> "BeautifulSoup" → For parsing HTML content  
-> "Pandas" → For creating and saving data in CSV format  

=>How to Run
-> Clone this repository or copy the script.  
-> Install the required libraries (if not installed yet):  

```bash
->pip install requests pandas beautifulsoup4 lxml
->python scraper.py
