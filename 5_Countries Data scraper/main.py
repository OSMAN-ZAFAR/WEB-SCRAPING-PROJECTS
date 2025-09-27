import requests 
import pandas as pd 
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0 Safari/537.36"
}

r = requests.get(url, headers=headers)
# print(r.status_code)
# print(r.text[:500])

soup=BeautifulSoup(r.text,"lxml")
table=soup.find("table",class_="wikitable")
# print(table)
header=table.find_all("th")
# print(header)
header_names=[]
for i in header:
    header_name=i.text
    header_names.append(header_name)
# print(header_names)  
df =pd .DataFrame(columns=header_names)
# print(df)
rows=table.find_all("tr")
# print(rows)
for i in rows[1:]:
    data=i.find_all("td")
    # print(data)
    row=[tr.text for tr in data]
    # print(row)
    l=len(df)
    df.loc[l]=row
# print(df)
df.to_csv("05_Countries Details.csv")
