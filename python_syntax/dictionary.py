cabinet={3:"hi",6:"bye"}
print(cabinet[3])
# print(cabinet[4]) 이렇게 입력할 경우 에러가 뜬다.
print(cabinet.get(3)) # 위의 경우와 비슷
print(cabinet.get(4)) # 이렇게 입력할 경우 에러가 뜨지 않고 none이라고 출력
print(cabinet.get(4,"해당하는 키가 없음")) # none 대신 뒤에 있는 입력 문구를 출력

print(3 in cabinet) # True
print(4 in cabinet) # False


# 문자열도 키로 사용 가능
cabinet={"key_3":"hi","key_6":"bye"}
print(cabinet["key_3"])

# 새로운 키 업데이트
cabinet["key_4"]="goodbye"
print(cabinet)

# 있던 키 삭제
del cabinet["key_4"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key 와 value 쌍으로 출력
print(cabinet.items())

# 모든 dictionary 값 삭제
cabinet.clear()
print(cabinet)