import os
import requests

urls_list=[]

def ans():
    
    print("\nWould you like to cheak the url again?")
    ask = str(input("Yes of No?\ny/n\n")).lower()
    if ask == "y" or ask == "n":
        if ask == "y" :
            main()
        else: 
            if ask == "n":
                print("Okay Bye-★")
                return
    else:
        print("You can only answer in y or n")
        ans()
        
def main():
    
    os.system("clear")
    print("\n★This is GGG world!★")
    print("I only like words that start with 'G'.")
    print("Let's cheak it out together!")
    print("Plz write any url you want!\n")
    
    urls=input("Write : ").lower().split(",")

    for url in urls:
        url=url.strip() 
        if "." not in url:
            print("Not in url format :( ")
        else:
            if "http://" not in url:
                url=f"http://{url}"
            try:
                request = requests.get(url)
                if request.status_code == 200:
                    print(url, "is..The url! \nAlmost there~")
                    if url[7] != "g" :
                        print("Can't come into GGG world.. SORRY!!") 
                    else:
                        print("YEAH!! Welcome to GGG country!!")
                        if url not in urls_list:
                            urls_list.append({url[7:-4].capitalize():str(url)})
                else:
                    print(url, "is NOT the url.. Bye..")  
            except:
                print(url, "is NOT the url.. Bye..")
    return ans()

main()