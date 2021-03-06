# ๐ ์น ์คํฌ๋ํ (Web Scraping)

## [Web Scraping](WS)

|No.|Content.|Remark.|
|------|-------|-------|
|1|[Html Code Change](WS/HtmlCodeChange.md)|์ ํ๋ธ ์ธ๋ค์ผ ๋ฐ๊พธ๊ธฐ|
|2|[GGG_world](WS/GGG_world.py)|url ๊ฒ์ฌ|
|3|[Wikipedia : ISO 3166-1](WS/ISO3166.py)|๊ตญ๊ฐ ๋์ด ๋ฐ ๊ฒ์ / url ์ ๊ณต|


<br>

## ์น ์คํฌ๋ํ์ด๋?

์น ์์ HTML์ ์ฝ์ด์ ํน์  ๋ฐ์ดํฐ๋ฅผ ์์งํ๋ ํ์ 

<br>

## ์น ์คํฌ๋ํ ๊ณผ์ 
1. ๋ฐ์ดํฐ ๊ฐ์ฒด ์ ์ + ์น ํ์ด์ง ์ ์ 
2. ์น ํ์ด์ง์์ ์ถ์ถํ  ๋ฐ์ดํฐ ๋ถ์
3. ์น์คํฌ๋ํ ์ฝ๋ ์์ฑ
4. ์ถ์ถํ ๋ฐ์ดํฐ ์ ์ฅ  

<br/>

## ์ธ๋ถ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ค์น    

### ๐ Request

Requests๋ HTTP ์์ฒญ์ ๋ณด๋ด๋ ๊ธฐ๋ฅ์ ์ ๊ณตํ๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ก HTTP GET, POST, PUT, DELETE ๋ฑ์ ์ฌ์ฉ ๊ฐ๋ฅํ๋ค.        
๋ํ dictionary๋ก ๋ง๋  ๋ฐ์ดํฐ๋ฅผ ํ์ํ request ์ธ์ฝ๋ฉ์ ์๋์ผ๋ก ์ฒ๋ฆฌํด์ค๋ค.        

``` python
import requests

url = "https://github.com/"
request = requests.get(url)                    # GET
print(request.text)                            # HTML ์ถ์ถ

url = "https://github.com/post"
dic={'kind':'zest', 'title':'Truffle', 'age':3}
request = requests.post(url, data=dic)         # POST
print(request.text)
```
https://github.com/psf/requests     
https://requests.readthedocs.io/projects/3/

<br>

### ๐ BeautifulSoup4

BeautifulSoup4์ ์น ํ์ด์ง ์ ๋ณด๋ฅผ ์คํฌ๋ฉํ๋ ๊ธฐ๋ฅ์ ์ ๊ณตํ๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ก HTML๊ณผ XML ๋ฌธ์ ๋ฑ์ ๋ถ์ํ๋ค.      

``` python
from bs4 import BeautifulSoup

url = "https://github.com/"
request = requests.get(url)  
soup = BeautifulSoup(request.text, 'html.parser')
```
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

<br/>

### ๐ Selenium

BeautifulSoup ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ง์ผ๋ก ๋ค์ํ ์ฌ์ดํธ์ ์ ๋ณด๋ฅผ ์ถ์ถํ  ์ ์์ง๋ง **์๋ฐ์คํฌ๋ฆฝํธ๋ก ๋์ ์ผ๋ก ์์ฑ๋ ์ ๋ณด๋ ๊ฐ์ ธ์ฌ ์ ์๋ค**๋ ํ๊ณ๊ฐ ์๋ค.      

๋ง์ฝ ์คํฌ๋ํ์ ์๋ํ๋ค๊ฐ ์๋ฌด ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์ค์ง ๋ชปํ๋ค๋ฉด ๋๋ถ๋ถ์ ๊ฒฝ์ฐ๊ฐ ์๋ฐ์คํฌ๋ฆฝํธ๋ก html์ ๋ง๋ค์ด์ ๊ทธ๋ ๋ค.   

<br>

๋ฐ๋ผ์ Selenium ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ฌ์ฉํ๋ ์ด์ ๋ ๋ค์๊ณผ ๊ฐ๋ค.

1. ์๋ฐ์คํฌ๋ฆฝํธ๊ฐ ๋์ ์ผ๋ก ๋ง๋  ๋ฐ์ดํฐ๋ฅผ ํฌ๋กค๋ง ํ๊ธฐ ์ํด
2. ์ฌ์ดํธ์ ๋ค์ํ  html ์์์ ํด๋ฆญ, ํค๋ณด๋ ์๋ ฅ ๋ฑ ์ด๋ฒคํธ๋ฅผ ์ฃผ๊ธฐ ์ํด
3. ๋ฐ๋ณต์ ์ผ๋ก ํ๋ ์น์์ ์๋ฌด ์๋ํ
    (ex. ์๋๋ก๊ทธ์ธ, ๋ธ๋ก๊ทธ ์ด์์๊ธ ์๋์ข์์์ ๋๊ธ ์์ฑ ๋ฑ)

``` python
from selenium import webdriver

url="http://google.com"

# driver ๊ฒฝ๋กํซ ํ์ผ๊ฒฝ๋ก์ ๊ฐ์ ๊ณณ์ ๋ ๊ฒฝ์ฐ
driver_same=webdriver.Chrome()
driver_same.get(url)

# driver ๊ฒฝ๋ก๋ฅผ ํ์ผ๊ฒฝ๋ก์ ๋ค๋ฅธ ๊ณณ์ ๋ ๊ฒฝ์ฐ
driver_diff=webdriver.Chrome("driver_diff์ ๊ฒฝ๋ก")
driver_diff.get(url)
```    
ํฌ๋กฌ๋๋ผ์ด๋ฒ ์ค์น : https://chromedriver.chromium.org/downloads

<br/><br>

## ๊ฐ๋จํ ์น ์คํฌ๋ํ

**Github ๋ธ๋ก๊ทธ ์ฒซ ํ์ด์ง์ ๋  ์๋ ํฌ์คํ url ์คํฌ๋กค๋ง ํ๊ธฐ**      

1. url ์ถ์ถ์ ์ํด ์ ์ ํ ์น ์ฌ์ดํธ๋ฅผ ์ผ๋ ์ํ์์ ```F12```๋ฅผ ๋๋ฌ html ์ฝ๋์ฐฝ์ ํจ๋ค.     
2. ```ctrl + shift + c```๋ฅผ ๋๋ฅธ ์ํ์์ ์ํ๋ ๊ณณ์ ํด๋ฆญํ๋ฉด ํด๋น ์์น์ ๋งค์นญ ๋๋ html ์ฝ๋๋ฅผ ๋ณผ ์ ์๋ค.       
3. ์น ์ฌ์ดํธ์์ ์ฝ๋์ฐฝ์ผ๋ก ๋์ด์ ํด๋น hmtl ์ฝ๋๋ฅผ ๋ง์ฐ์ค ์ค๋ฅธ์ชฝ ๋ฒํผ์ผ๋ก ํด๋ฆญํ๋ฉด ๋จ๋ ์ฐฝ ์ค ```Copy``` > ```copy selector``` ๋ฅผ ์ ํํ๋ฉด ์ํ๋ ์ ๋ณด์ hmtl ์์น๊ฒฝ๋ก๋ฅผ ๋ณต์ฌํ๊ฒ ๋๋ค.         
4. find, find_all ํน์ select ํจ์ ๋ฑ๊ณผ html ์์น๊ฒฝ๋ก๋ฅผ ์ฌ์ฉํ์ฌ ํ์ํ ๋ฐ์ดํฐ๋ฅผ ์ถ์ถํ๋ค.    

<br/>

**html์ฝ๋์ฐฝ ์์** 

![gitblog](https://user-images.githubusercontent.com/56749776/129632160-620694b6-0632-40d0-aa8d-ff409eb02ef5.png)

<br>

**์ฝ๋**

``` python
import requests
from bs4 import BeautifulSoup

url = "https://github.blog/"
request = requests.get(url)  
soup = BeautifulSoup(request.text, "html.parser")
results = soup.select("#main > section > div > div > div")
count=1

for result in results:
    https=result.find("a")
    link=https.attrs['href']
    print(f"# {count} : ",link)
    count+=1
```

<br>

**๊ฒฐ๊ณผ**

```
# 1 :  https://github.blog/2021-08-11-githubs-engineering-team-moved-codespaces/
# 2 :  https://github.blog/2021-08-11-githubs-engineering-team-moved-codespaces/
# 3 :  https://github.blog/2021-08-16-securing-your-github-account-two-factor-authentication/
# 4 :  https://github.blog/2021-08-12-teaching-learning-github-classroom-visual-studio-code/
# 5 :  https://github.blog/2021-08-12-whats-new-from-github-changelog-july-2021-recap/
# 6 :  https://github.blog/category/community/
# 7 :  https://github.blog/category/education/
# 8 :  https://github.blog/category/engineering/
# 9 :  https://github.blog/category/enterprise/
# 10 :  https://github.blog/category/open-source/
# 11 :  https://github.blog/category/policy/
# 12 :  https://github.blog/category/product/
# 13 :  https://github.blog/category/security/
```
