# print("dks","sud","gk","tp",sep=" : ",end="?")
# # 끝에 물음표가 붙으며 print 문이 끝나고 ,자리에 : 로 단어들이 구분된다.
# print("핳","하","하","예","?")
# #앞에 문장이 물음표로 끝났기 때문에 문장이 구분되지 않고 이어져서 나온다.

# scores={"수학":100, "영어":40, "물리":100}
# for sub,score in scores.items():
#     # print(sub,score)
#     print(sub.ljust(8),str(score).rjust(4),sep=":")

# for i in range (10):
#     print("번호 :",str(i).zfill(3))

# # 출력의 다양한 형태
# # 빈자리는 빈 공간으로 두고 오른쪽 정렬 10자리 확보
# print("{0: >10}".format("300"))

# # 같은 조건에 양수일 때 +, 음수일 때 - 표시
# print("{0: >+10}".format(300))
# print("{0: >+10}".format(-300))

# # 왼쪽 정렬, 빈칸 /로 채움
# print("{0:/<+10}".format(300))

# # 3자리마다 콤마 찍어주기
# print("{0:,}".format(30000000))

# # 3자리마다 콤마 찍고 +- 부호 붙이기
# print("{0:+,}".format(30000000))

# # 3자리마다 콤마 찍고 +- 부호 붙이고 자릿수 확보
# # 빈자리 ^로 채우기
# print("{0:^<+30,}".format(30000000))

# # 소수점 표현
# print("{0:f}".format(5/3))

# # 소수점 2째 자리까지 표현 (3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))


