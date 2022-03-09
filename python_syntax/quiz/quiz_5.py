# 승객 50명
# 탑승 시간 5~50분
# 5~15분 사이 승객만 탑승시킴
# 총 승객 수
from random import *
count=0
for i in range(1,51):
    ride=randrange(5,51)
    if ride>15:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i,ride))
    else:
        print("[0] {0}번째 손님 (소요시간: {1}분)".format(i,ride))
        count+=1

print("총 탑승 승객 : %d"%count)