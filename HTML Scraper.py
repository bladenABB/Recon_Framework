from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.info-clipper.com/en/companies/russia.ru/rostov-on-don.html")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
companies = soup.find_all("span", attrs={"class":"i_company"})

file = open("rostov_companies.csv", "w")
writer = csv.writer(file)

writer.writerow(["COMPANIES"])

for company in companies:
    print(company.text)
    writer.writerow([company.text])
file.close()
    
