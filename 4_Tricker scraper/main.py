import requests
import pandas as pd 
from bs4 import BeautifulSoup
url="https://ticker.finology.in/market/52-week-high"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
# fetching the companies names
names=soup.find_all("td", class_="left")
company_names=[]
for i in names:
    name=i.get_text(strip=True)
    company_names.append(name)
# print(company_names)    
# fetching the prices
prices=soup.find_all("td",class_="Number")
price_list=[]
for i in prices:
    price=i.get_text(strip=True)
    price_list.append(price)
high_price=soup.find_all("span",class_="Number")
high_price_list=[]
for i in high_price:
    high=i.get_text(strip=True)
    high_price_list.append(high)

# # print(price_list)    
df=pd.DataFrame({"Company":company_names,
                     "Prices":price_list,
                     "Day High Prices":high_price_list
                     })
# print(df)
df.to_csv("04_Tricker Details.csv")
