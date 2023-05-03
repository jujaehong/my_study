# 데이터 수집단계

# 데이터 수집 - > 데이터 분석/처리 -> 인공지능 모델학습 -> 인공지능 모델평가 ->  사용

# 데이터 수집 : 원하는 데이터들을 모아오는것.
# 데이터 분석 : 좋은데이터만 거르는것.

# http (hypertext transfer protocol) 
# request(요청) - response(응답)
# client : request(웹브라우저(크롬,엣지 등등....)) <---> server : response
# html(hypertext markup language) <--- response(응답)을 까보면 html이 있는것이다.
# <html></html>
# html 파싱

# import requests

# url = "https://www.naver.com/"
# response = requests.get(url)
# status = response.status_code
# html = response.text
# print(status)
# print(html)


# http 상태코드
# 200 : ok
# 요청 성공
# 302 : 리다이렉트
# 다른 페이지로 바로 연결
# 400 :  Bad Request 요청이 잘못됨
# 401 : Unauthorized 비인증됨
# 403 : Forbiddrn 접근 권한 없음
# 404 : Not Found 요청받은 내용이 없음
# 405 : Method Not Allowed 접근 방법이 잘못됨

# 500 : Internal Server Error 서버에러
# 501 : Not Implemented
# 502 : Bad Gateway 잘못된 응답

# url 구조
# http://naver.com/blog/?~~~~~
# 프로토콜 ://호스트주소:포트번호/경로?쿼리
# 호스트주소 : 인터넷 주소 
# 포트번호 : 
# 경로 : 
# 쿼리 : 경로와 다른게 추가적인 데이터
# 쿼리이름=값&쿼리이름=값&쿼리이름=값


# import requests

# search_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="

# keyword = input("검색어 입력 : ")
# url = search_url + keyword
# response = requests.get(url)
# print(response.text)
## print(type(response.text)) # 타입을 확인하는 소스 ( 결과 : 문자열 )


# BeautifulSoup
# html 파싱(parsing)
# html을 객체 구조화해서 사용

# from bs4 import BeautifulSoup
# html 태그
# <태그이름 속성=속성값>내용</태그이름>
# <html><head></head><body></body>
# html.head 파이썬 객체화를 해주는 것이 BeautifulSoup이다.
# html.body 파이썬 객체화를 해주는 것이 BeautifulSoup이다.

# html = "<html><body>Hello</body></html>"
# soup = BeautifulSoup(html, "html.parser") #객체로 만들 문서정보를 넣어주어야 한다. , 어떤형식으로 파싱할 것인지를 넣어준다.
# print(soup.body.text)
# print(type(soup.body.text))

# import requests
# from bs4 import BeautifulSoup
# import os

# search_url = "https://www.google.com/search?tbm=isch&q="
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img')

# folder_name = "imgs"
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)

# for idx, img in enumerate(imgs[1:]): # 첫 번째 이미지는 로고 이미지이므로 생략
#     print(f"{idx}번째 이미지 저장 완료")
#     file_name = f"img_{idx}.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_respones = requests.get(img['src'])
#     img_data = img_respones.content
#     with open(file_path, "wb") as f:
#         f.write(img_data)

# enumerate(이터러블) # idx(인덱스) 번호를 붙여주는 함수 
# li1 = ["김연아", "류현진", "손흥민"]
# for name in enumerate(li1):
#     print(name)


# 네이버 IT/과학 뉴스 크롤링
import requests
from bs4 import BeautifulSoup
import os
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# headers={"User-Agent":"Mozilla/5.0"} ---> 크롤링 방지 회피
response = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
html = response.text
soup = BeautifulSoup(html, "html.parser")
div = soup.body.find('div', attrs={'class': 'list_body'})
headlines = div.find_all('a', attrs={'class': 'cluster_text_headline'})


folder_name = "crawling_result"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for headline in headlines:

    # 과제 : crawling_result 폴더의 headlines.txt 파일에 저장
    # headlines.txt 파일에 저장하기

    # print(headline.text.strip())

    # with open("crawling_result/headlines.txt","a", encoding="utf-8") as f:
    #     f.write(headline.text.strip())
    #     f.write("\n")

    article_response = requests.get(headline['href'])
    article_soup = BeautifulSoup(article_response.text, "html.parser")
    article = article_soup.find('div', attrs={"id":"dic_area"})
    print(article.text)


