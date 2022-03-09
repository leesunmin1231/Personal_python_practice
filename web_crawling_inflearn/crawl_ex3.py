# css selector 이용하기.

import requests
from bs4 import BeautifulSoup

res=requests.get('https://polarmin.tistory.com/m') # 웹페이지 가져오기.
soup=BeautifulSoup(res.content,'html.parser') #웹페이지 파싱하기.
data=soup.select('strong')
# for item in data:
    # print(item.get_text())
    
    
title=soup.select('header strong') # header 태그 안에 있는 strong 태그 
# 태그 안에 있는 모든 태그 가능
# header > strong으로 적을 경우 header 바로 밑에 태그가 strong인 경우.
for item in title:
    print(item.get_text())
    
data=soup.select('.tit_blog') 
# class이름 으로도 가져올 수 있다. id는 #id이름 으로 적으면 된다.
# 'strong.tit_blog' 로 쓸 수 있다. strong 태그에 tit_blog class
# class 이름에 공백이 있을 경우 .으로 연결
# 예를 들어 'tit blog' -> '.tit.blog'

for item in data:
    print(item.get_text())