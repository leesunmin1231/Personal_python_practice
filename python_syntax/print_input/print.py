# print하는 다양한 방법
print("a"+"b")
name="이선민"
print("a",name,"b")

# %이용
print("안녕하세요 저는 %s 입니다" % "이선민")
print("저는 %d 살 입니다."%23)
print("안녕하세요 저는 %s 이고, %d 살 입니다."%("이선민",23))


# .format 이용
print("저는 {} 살 입니다.".format(23))
print("안녕하세요 저는 {} 이고, {} 살 입니다.".format("이선민",23))
print("안녕하세요 저는 {1} 이고, {0} 살 입니다.".format("이선민",23)) # format 단어를 어디에 넣을지 지정 가능

print("안녕하세요 저는 {name} 이고, {age} 살 입니다.".format(name="이선민",age=23)) 

# f이용
name="이선민"
age=23
print(f"안녕하세요 저는 {name} 이고, {age} 살 입니다.") # f 이용
