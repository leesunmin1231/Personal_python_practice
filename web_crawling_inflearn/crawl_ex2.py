# div 태그 내에 있는 또 다른 태그에 있는 텍스트 가져오기

import requests
from bs4 import BeautifulSoup

res=requests.get('https://polarmin.tistory.com/29') # 웹페이지 가져오기.
soup=BeautifulSoup(res.content,'html.parser') #웹페이지 파싱하기.
data=soup.find('div',class_="hgroup")
title=data.find('h1')
print(title.get_text())