import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

url = "https://ko.wikipedia.org/wiki/ISO_3166-1"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
results = soup.select("table tbody tr")

for result in results:
    country=result.find("span", {"flagicon"})
    print(country)

#mw-content-text > div.mw-parser-output > table.wikitable.sortable.jquery-tablesorter