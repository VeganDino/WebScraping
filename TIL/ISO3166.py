import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

url = "https://ko.wikipedia.org/wiki/ISO_3166-1"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
results = soup.find("table").find_all("tr")[1:]

ISO=[]

for result in results:
    content=result.find_all("td")
    name=content[0].text
    alpha=content[1].text
    href=content[0].find_all("a")[1].attrs["href"]
    link=f"https://ko.wikipedia.org{href}"

    if name and alpha and link:
        country={
            'name':name,
            'alpha_code':alpha,
            'link':link
        }
        ISO.append(country)
        
def ask():
    print("\nPick one country by number.\n")
    try:
        choice=int(input("▸ "))
        if choice<=0 or choice>len(ISO):
            print("Off the list! Pick it up again!\n")
            ask()
        else:
            num=ISO[choice-1]
            print(f"No.{choice} is the country{num['name']}.")
            print(f"Information about{num['name']} is in the this link.\n{num['link']}")
            restart()
    except ValueError:
        print("Wrong input. Please enter it correctly.\n")
        ask()

def restart():
    ans = str(input("Do you want to do it again? y/n\n")).lower()
    if ans=='y' or ans=='n':
        if ans=='y':
            ask()
        elif ans=='n':
            print('Good bye! -END-')
            return
    else:
        print("Please choose between y and n.")
        restart()
    
print("◤ Wikipedia : ISO 3166-1 ◢")
print("Components of the main unit of the country\n")
for idx, val in enumerate(ISO):
    print(f"▸ {idx+1} :{val['name']} ({val['alpha_code']})")
ask()
