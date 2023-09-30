# recon_scraper.py

# Web scraping tool using proxy servers for anonymity. Changes user-agent, and identifies cookies from the target server.

# Author Brian Bladen

import requests

proxies = {"http": "45.14.174.5:80"}
headers = {"user-agent": "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops", proxies=proxies, headers=headers)
print(r.text)
for cookie in r.cookies:
    print(cookie)
print(r.cookies["TestingGround"])
