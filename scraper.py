import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

	
URL = "https://www.amazon.com.au/Call-Duty-Vanguard-PlayStation-5/dp/B09D3J18HC/ref=sr_1_3?crid=30IXKHFREHGZ3&keywords=ps5&qid=1655006585&sprefix=p%2Caps%2C298&sr=8-3"
webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "lxml")

title = soup.find("span", attrs={"id":'productTitle'})
price = soup.find("span", attrs={"class":'a-price aok-align-center reinventPricePriceToPayMargin priceToPay', "class":'a-offscreen'})

title_value = title.string.strip()
price_value = price.string.strip()

print("Name: " + title_value)
print("Price: " + price_value)