import requests
from bs4 import BeautifulSoup

res=requests.get('https://comic.naver.com/webtoon/weekday?order=User') # 웹페이지 가져오기.
soup=BeautifulSoup(res.content,'html.parser') #웹페이지 파싱하기.
data=soup.find_all('div',class_="col_inner")
for daily_list in data:
    print("\n")
    title=daily_list.find('span')
    print(title.get_text())
    lst=daily_list.find_all('a',class_='title')
    for index,name in enumerate(lst):
        if index==len(lst)-1:
            print(str(index+1)+'. '+name.get_text())
            break
        print(str(index+1)+'. '+name.get_text(),end=', ')