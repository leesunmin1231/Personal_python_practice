# score_file=open("score_text.txt","w",encoding="utf8") 
# # w는 쓰는 용도
# print("수학 : 100", file=score_file)
# print("영어 : 30",file=score_file)
# score_file.close()

# score_file=open("score_text.txt","a", encoding="utf8")
# # a는 append 추가하는 용도
# print("자료구조 : A+", file=score_file)
# score_file.write("컴퓨터 통신 : A+")
# score_file.write("\n비쥬얼 프로그래밍: A+") 
# # write로 쓴 문장은 print와 다르게 자동으로 줄바꿈이 되지 않기 때문에
# #/n을 넣어 주어야 한다.
# score_file.close()
# # a로 하고 반복해서 실행하면 .write로 쓴 부분은 실행할 때마다 또 추가되지만
# # print로 쓴 구문은 처음 한번만 추가되고 그 이후에는 추가 되지 않는다.

# score_file=open("score_text.txt","r",encoding="utf8")
# #print(score_file.read())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file=open("score_text.txt","r",encoding="utf8")
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     else:
#         print(line,end="")
# score_file.close()

# 리스트 형태로 불러오기
score_file=open("score_text.txt","r",encoding="utf8")
line=score_file.readlines()
print(line)
for line in line:
    print(line,end="")
