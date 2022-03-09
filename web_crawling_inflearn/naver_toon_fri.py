import requests
from bs4 import BeautifulSoup

res=requests.get('https://comic.naver.com/webtoon/weekdayList?week=fri') # 웹페이지 가져오기.
soup=BeautifulSoup(res.content,'html.parser') #웹페이지 파싱하기.

day_data=soup.find('div',class_='view_type')
day=day_data.find('h3',class_='sub_tit')
print(day.get_text())
data=soup.select('div.list_area.daily_img li')
dic={}
for item in data:
    title=item.select_one('dt a')
    author=item.select_one('dd a')
    rate=item.select_one('div.rating_type strong')
    dic[float(rate.get_text())]=[title.get_text(),author.get_text()]

sort_dic=sorted(dic.items(),reverse=True)
print("별점순")
for rate,others in sort_dic:
    if rate<9.9:
        break
    print("제목: {} 저자: {} 평점:{}".format(others[0],others[1],rate))
print("\n인기순, 평점 9.9 이상")
for rate,others in dic.items():
    if rate<9.9:
        continue
    print("제목: {} 저자: {} 평점: {}".format(others[0],others[1],rate))
