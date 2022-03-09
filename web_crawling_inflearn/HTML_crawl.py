from bs4 import BeautifulSoup # 웹페이지 파싱하는 라이브러리
html="""
<html>
    <body>
        <h1 id='title'>[1]크롤링이란?</h1>
        <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p>
        <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p>
    </body>
</html>
"""

soup=BeautifulSoup(html,"html.parser")

# 태그로 검색하는 방법
data =soup.find('p')
print(data.string) # data.get_text()와 같다.

# 태그와 태그에 있는 속성으로 검색하기.
data1 =soup.find('p', class_='cssstyle') # class요소를 검색할 때는 반드시 뒤에 _를 붙여주어야 한다. 
data2 =soup.find('p', 'cssstyle')
data3 =soup.find('p', attrs={'id': 'body','align':'center'})
data4 =soup.find(id='body') # id는 태그 없이 검색 가능 (얘만 가지고 있는 별칭 느낌.)
# print (data1.string)
# print (data2.string)
# print (data3.string)
# print (data4.string)

# 찾고자 하는 태그에 해당하는 모든 데이터를 가져오기.
data_all=soup.find_all('p')
for item in data_all:
    print(item.string)
    