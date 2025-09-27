import requests
import pandas
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")

names=soup.find_all("a",class_="title")
product_names=[]
for i in names:
    name = i.get_text().strip()
    product_names.append(name)
# print(product_names)    

prices=soup.find_all("h4",class_="price")
product_prices=[]
for i in prices:
    price=i.get_text().strip()
    product_prices.append(price)
# print(product_prices)

descriptions=soup.find_all("p",class_="description")
product_descriptions=[]
for i in descriptions:
    description=i.get_text().strip()
    product_descriptions.append(description)
# print(product_descriptions )

reviews=soup.find_all("p",class_="review-count float-end")
product_reviews=[]
for i in reviews:
    review=i.get_text().strip()
    product_reviews.append(review)
# print(product_reviews)    

df=pandas.DataFrame({"product_name":product_names,"product_price":product_prices,"product_description":product_descriptions,"product_review":product_reviews})
# print(df)
df.to_csv("Tablets Data.csv")