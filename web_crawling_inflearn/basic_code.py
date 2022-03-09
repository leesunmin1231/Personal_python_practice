import requests

from bs4 import BeautifulSoup # 웹페이지 파싱하는 라이브러리
# 파싱이란? 문자열을 해석하는 것. 여기서는 html문서


res=requests.get('https://polarmin.tistory.com/29') # 웹페이지 가져오기.

soup=BeautifulSoup(res.content,'html.parser') #웹페이지 파싱하기.

# ( 분석할 html 문서, html을 분석하는 일종의 메소드)

mydata=soup.find('title') # 필요한 데이터 추출하기. 

#soup.find() 함수로 원하는 부분을 지정.

print(mydata)

print(mydata.get_text()) # 추출한 데이터 활용하기.

# get_text() 텍스트만 가져옴.

