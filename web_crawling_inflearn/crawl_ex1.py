# 웹페이지 일정한 규칙 있는 목록 가져오기.

import requests
from bs4 import BeautifulSoup

res=requests.get('https://polarmin.tistory.com/29') # 웹페이지 가져오기.
soup=BeautifulSoup(res.content,'html.parser') #웹페이지 파싱하기.
data=soup.find_all('p',attrs={'data-ke-size': "size16"})
for item in data:
    if item.get_text()=='&nbsp;':
        continue
    print(item.get_text())
