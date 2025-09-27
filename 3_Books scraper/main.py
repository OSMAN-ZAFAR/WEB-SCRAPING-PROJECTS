import requests
import pandas
from bs4 import BeautifulSoup
url="http://books.toscrape.com/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")

Books=soup.find_all("h3")
Books_tittle=[]
for i in Books:
    Book=i.get_text()
    Books_tittle.append(Book)
# print(Books_tittle)   

Books=soup.find_all("p",class_="price_color")
Books_price=[]
for i in Books:
    Book=i.get_text()
    Books_price.append(Book)
# print(Books_price)

Books=soup.find_all("p",class_="instock availability")
Books_availability=[]
for i in Books:
    Book=i.get_text(strip=True)
    Books_availability.append(Book)
# print(Books_availability)    

df=pandas.DataFrame({"Book Title":Books_tittle,"Boooks Price":Books_price,"Books Availability":Books_availability})
# print(df)
df.to_csv("Books Details.csv")