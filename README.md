# 📑 WebScraping

## 웹 스크래핑 (Web Scraping)   

웹 상의 HTML을 읽어와 특정 데이터를 수집하는 행위 

<br>

## 웹 스크래핑 과정
1. 데이터 객체 정의 + 웹 페이지 선정
2. 웹 페이지에서 추출할 데이터 분석
3. 웹스크래핑 코드 작성
4. 추출한 데이터 저장  

<br/>

## 외부 라이브러리 설치    

> Request

Requests는 HTTP 요청을 보내는 기능을 제공하는 라이브러리로 HTTP GET, POST, PUT, DELETE 등을 사용 가능하다.        
또한 dictionary로 만든 데이터를 필요한 request 인코딩을 자동으로 처리해준다.        

``` python
import requests

url = "https://github.com/"
request = requests.get(url)                    # GET
print(request.text)                            # HTML 추출

url = "https://github.com/post"
dic={'kind':'zest', 'title':'Truffle', 'age':3}
request = requests.post(url, data=dic)         # POST
print(request.text)
```
https://github.com/psf/requests     
https://requests.readthedocs.io/projects/3/

<br/>

> BeautifulSoup4

BeautifulSoup4은 웹 페이지 정보를 스크랩하는 기능을 제공하는 라이브러리로 HTML과 XML 문서 등을 분석한다.      

``` python
from bs4 import BeautifulSoup

url = "https://github.com/"
request = requests.get(url)  
soup = BeautifulSoup(request.text, 'html.parser')
```
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

<br>

## 간단한 웹 스크래핑

🎈 깃허브 블로그 첫 페이지에 떠 있는 포스팅 스크롤링 하기

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

결과
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
