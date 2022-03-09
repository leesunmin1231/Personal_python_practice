import requests
res=requests.get("http://naver.com")
'''
print("응답코드:",res.status_code)  #200 이면 정상

if res.status_code == requests.code.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드",res.status_code,"]")
'''
res.raise_for_status() #응답코드가 200이 아닐 경우 오류를 내서 프로그램 종료시킴

print(len(res.text))
with open("mygoogle.html","w",encoding="utf8")as f:
    f.write(res.text)