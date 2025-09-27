import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.amazon.com/s?k=oppo+phone&rh=n%3A21514055011&dc&crid=MORIM43E6NWW&qid=1758864530&rnid=85457740011&sprefix=oppo%2Caps%2C441&ref=sr_nr_p_123_1&ds=v1%3AfvXIgvJZ9wxkpZrXh4hipsQn4e%2FZSyDRZX9cQczCfGs"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,"lxml")
print(r.status_code)

Links=[]
Details=[]
Prices=[]
Availability=[]
Ratings=[]

links=soup.find_all("a",class_="a-link-normal s-line-clamp-2 s-link-style a-text-normal")

details=soup.find_all("h2",class_="a-size-medium a-spacing-none a-color-base a-text-normal")

prices=soup.find_all("span",class_="a-price-whole")

availabilitys=soup.find_all("span",class_="a-size-base a-color-price")

ratings=soup.find_all("span",class_="a-size-small a-color-base")

from itertools import zip_longest
for l,d,p,a,r in zip_longest(links,details,prices,availabilitys,ratings,fillvalue=None):
    link="https://www.amazon.com" + l.get("href").strip() if l else "N/A"
    detail=d.text.strip() if d else "Product details are not given"
    price=p.text.strip() if p else "Price is not given"
    availability=a.text.strip() if a else "Availability is not given"
    rating=r.text.strip() if r else "Rating is not given"


    Links.append(link)
    Details.append(detail)
    Prices.append(price)
    Availability.append(availability)
    Ratings.append(rating)

df=pd.DataFrame({
    "Product Details":Details,
    "Prices":Prices,
    "Availability":Availability,
    "Ratings":Ratings,
    "Product Link":Links
})
df.to_csv("Amazon Products.csv",index=False)
    