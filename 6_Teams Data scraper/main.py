import requests
import pandas as pd 
from bs4 import BeautifulSoup
headers_list=[]
for page in range(1,11):
    url="https://www.scrapethissite.com/pages/forms/?page="+str(page)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    table=soup.find("table",class_="table")
    
    if page==1:
        headers=table.find_all("th")
        for i in headers:
            header=i.text.strip()
            headers_list.append(header)
        df=pd.DataFrame(columns=headers_list)
    rows=table.find_all("tr")
    for i in rows[1:]:
        data=i.find_all("td")
        row=[tr.text.strip() for tr in data]
        l=len(df)
        df.loc[l]=row
df.to_csv("06_Team Details.csv",index=False)  
# print(len(df))      