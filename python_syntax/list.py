subway=[10,20,30]
print(subway.index(10))

subway.append(40) # 맨뒤에 객체 추가
print(subway)

subway.insert(1,15) # index 먼저 입력 후 넣을 객체 입력
print(subway)

subway.pop() # 맨뒤에 있는 객체 삭제
print(subway)

subway.append(20)
print(subway.count(20)) # 중복되는 객체 개수 세기

subway.reverse() # 객체 거꾸로 정렬
print(subway)

subway.sort() # 객체 순서대로 정렬
print(subway)

subway.clear() # 리스트 내에 객체 전부 삭제
print(subway)

mix_list=["hi",20,True] # 다양한 자료형 함께 넣는 것 가능
subway.extend(mix_list) # 두개 list 합치기
print(subway)