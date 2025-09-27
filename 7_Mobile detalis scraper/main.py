import requests
import pandas as pd
from bs4 import BeautifulSoup

name_list,price_list,disc_list,rev_list=[],[],[],[]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.1 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://priceoye.pk/",
}

for page in range(1,10):
    url=f"https://priceoye.pk/mobiles?page={page}"
    r=requests.get(url,headers=headers)
    # print(r)
    soup=BeautifulSoup(r.text,"lxml")

    names=soup.find_all("div",class_="p-title p-title-center bold h5")

    prices=soup.find_all("div", class_="price-box p1")
    
    discs=soup.find_all("div",class_="price-diff-saving")
    
    revs=soup.find_all("div", class_="user-rating-content")

    from itertools import zip_longest
    for n,p,d,r_ in zip_longest(names,prices,discs,revs,fillvalue=None):
        name=n.text.strip() if n else "N/A"
        price=p.text.strip() if p else "N/A"
        disc=d.text.strip() if d else "No Discount"
        rev=r_.text.strip() if r_ else "No Reviews"

        # Here we are using the itertools because we have different list with different length. In dataframe if the length of all list are not equal then complier give error that all the list has must equal length .To avoid this error we use the zip_longest function. It work such that it forcfully made the all list in equal length and also give us the permission if we want to add an other message .

        name_list.append(name)
        price_list.append(price)
        disc_list.append(disc)
        rev_list.append(rev)

# print(len(name_list))
# print(len(price_list))
# print(len(disc_list))
# print(len(rev_list))

df=pd.DataFrame({
    "Mobile Name":name_list,
    "Price":price_list,
    "Discount":disc_list,
    "Reviews":rev_list
})

# print(df)
df.to_csv("07_Mobiles Details.csv",index=False)        