# 🤲 유튜브 썸네일 내 멋대로 바꾸기

<br>

유튜브(Youtube)는 전세계적으로 최대 규모의 동영상 공유 플렛폼이다.   
홈페이지를 클릭하면 첫 화면에 나란히 정렬되어 업로드 된 영상들의 썸네일을 볼 수 있다.      
본인은 유튜브 최상단에 있는 영상들의 썸네일과 제목, 조회수, 아이디 등을 바꿔보고자 한다.    

<br>

이 과정은 HTML 코드만 바꿔주면 되기 때문에 별도의 코딩이 필요하지 않다.    
또한 겉모습만 바뀌었을뿐 영상을 클릭하면 본래의 영상을 시청할 수 있다.    

<br>

유튜브 사이트를 열었을 때 처음 보이는 화면은 다음과 같다.   

<br>

![youtube_change1](https://user-images.githubusercontent.com/56749776/129781566-a7f3f0a9-d8e2-453d-a808-b912f283332d.png)

<br>

처음 시작으로 두 번째 영상의 썸네일을 바꿔보자.     
(여자아이들이라고 적혀있는 빨간 썸네일이 두 번째 영상이다.)   

<br>

바꾸고자 하는 사진에 대한 데이터를 추출을 위해 ```F12```를 눌러 html 코드창을 킨다.     
```ctrl + shift + c```를 누른 상태에서 바꿀 썸네일을 클릭하면 해당 사진의 위치와 매칭 되는 html 코드를 찾을 수 있다.       

<br>

![youtube_change2](https://user-images.githubusercontent.com/56749776/129781574-f5017fea-a43c-4c00-822c-65c67c171de9.png)

<br>

옅은 회색빛으로 그림자가 저있는 html을 보면 url로 표시되어있다.         
썸네일은 이미지의 주소로 코드에 적혀있기 때문이다.        
따라서 썸네일을 바꾸기 위해 간단히 이미지의 주소만 바꾸면 된다.        

본인은 썸네일을 바꾸기 위해 pixabay라는 무료 이미지 사이트를 이용했다.      
사용하고자 하는 사진을 마우스 오른쪽 버튼으로 누르면 다음과 같은 창이 뜬다.  

<br>

![youtube_change4](https://user-images.githubusercontent.com/56749776/129784449-e27a981a-7109-48a9-8cc2-9c5f6264e6e6.png)

<br>

4번 째 칸에 보이는 ```이미지 주소 복사```를 누르면 자동으로 복사가 된다.     
다시 html 코드창으로 돌아가 기존의 이미지 주소를 복사한 이미지 주소로 바꿔준 후 ```Enter```를 누르면 썸네일이 바뀌어져 있는 것을 확인 할 수 있다.     

<br>

썸네일만 이미지 주소가 필요하며 제목, 조회수, 아이디 등은 사진과 같은 방법으로 하되 문자이므로 원하는 문장 혹은 단어, 숫자 등으로 바꿔주면 된다.      

<br>

최종적으로 홈페이지 상단에 자리잡고 있던 4개의 영상 썸네일을 바꾼 모습은 다음과 같다. 

<br>

![youtube_change3](https://user-images.githubusercontent.com/56749776/129781609-b81f3225-948a-456f-ad9a-77ace80a9646.png)

<br>

바꾼 부분만 확대한 캡쳐본   

<br>

![youtube_change5](https://user-images.githubusercontent.com/56749776/129785466-f67f5705-3b97-4abe-8ae9-d60f79e5c8d1.png)

<br>

Youtube : https://www.youtube.com/      
Pixabay : https://pixabay.com/ko/