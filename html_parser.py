from bs4 import BeautifulSoup
import requests
import csv

proxies = {"http": "45.14.174.5:80"}
headers = {"user-agent": "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}

page_to_scrape = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops", proxies=proxies, headers=headers)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
description = soup.find_all("p", attrs={"class":"description"})
price = soup.find_all("h4", attrs={"class":"pull-right price"})

file = open("test_ecommerce.csv", "w")
writer = csv.writer(file)

writer.writerow(["DESCRIPTIONS","PRICES"])

for description, price in zip(description, price):
    print(description.text + " - " + price.text)
    writer.writerow([description.text, price.text])
file.close()
    
