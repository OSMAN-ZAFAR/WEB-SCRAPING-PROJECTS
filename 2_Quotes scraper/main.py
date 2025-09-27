import requests
from bs4 import BeautifulSoup
import pandas
url="http://quotes.toscrape.com/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")

qoutes=soup.find_all("span",class_="text")
qoutes_text=[]
for i in qoutes:
    qoute=i.get_text().strip()
    qoutes_text.append(qoute)
# print(qoutes_text)    

authors=soup.find_all("small",class_="author")
authors_name=[]
for i in authors:
    author=i.get_text().strip()
    authors_name.append(author)
# print(authors_name)

df=pandas.DataFrame({"Qoutes":qoutes_text,
                     "Authors Name":authors_name
                     })

df.to_csv("Quotions.csv",index=True)