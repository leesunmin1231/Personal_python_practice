# 문자열
name="이선민"
print(name)
sentence="""
안녕하세요
반갑습니다.
"""
print (sentence)

# slicing (슬라이싱)
print(name[1])
print(name[0:2]) # 0부터 2직전까지, 즉 0부터 1까지
print(name[:3]) # 처음부터 3직전까지
print(name[0:]) # 0에서 부터 끝까지
print(name[-2:]) # 뒤에서 두번째에서 부터 끝까지

python="Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자인지 확인
print(len(python))
print(python.replace("Python", "Java"))

index=python.index("n") # n 의 위치를 찾아준다.
print (index)
index=python.index("n",index+1) # index+1 위치부터 시작해서 n을 찾아준다. (여기서는 6부터 찾기 시작)
print (index)

print(python.find("n")) # index와 바슷한 기능
print(python.find("java")) # 없는 단어를 찾을 경우 -1을 반환
# print(python.index("java")) # 그러나 index의 경우 없는 단어를 찾을 경우 오류가 난다.

print(python.count("n")) # n의 개수를 세어줌
