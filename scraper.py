import bs4
import requests

res = requests.get("https://www.amazon.com.au/Call-Duty-Vanguard-PlayStation-5/dp/B09D3J18HC")

soup = bs4.BeautifulSoup(res.text, "lxml")
title = soup.find(id="productTitle").text
price = soup.find(class_="a-offscreen").text

print("Title: " + title.strip())
print("Price: " + price)