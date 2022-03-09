#표준 체중을 구하는 프로그램
def std_weight(height,gender):
    if gender=="남자":
        h=float(height)/100
        weight=h*h*22
    elif gender=="여자":
        h=float(height)/100
        weight=h*h*21
    else:
        print("성별을 다시 입력하십시오.")

    return weight
height=158
gender="여자"
weight=std_weight(height,gender)
print("키 {}cm {}의 표준체중은 {}kg 입니다.".format(height,gender,round(weight,2)))
