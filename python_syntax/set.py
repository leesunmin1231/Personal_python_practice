# 집합
# 중복 안됨, 순서 없음
any={1,2,3,3,3}
print(any)

java={"h","l","k","3"}
python=set(["1","2","3","4"])

# 공통 인수 찾기
print(java&python)
print(java.intersection(python))

# 합집합
print(java|python)
print(java.union(python))

# 차집합
print(java-python)
print(java.difference(python))

# 요소 추가
java.add("23")
print(java)

# 요소 제거
python.remove("4")
print(python)