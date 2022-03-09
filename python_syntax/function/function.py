# 파이썬에서 2개 값 튜플 형식으로 리턴 가능

def addmoney(balance, add):
    return balance+add

balance=addmoney(50000,20000)
print("{}원 입금이 완료 되었습니다. 잔액은 {}원 입니다.".format(20000,balance))

def withdraw(balance, out):
    commision=100
    return commision,balance-out-commision  # 두가지 값 튜플형식으로 리턴

commision,balance=withdraw(balance,30000)
print("{}원 출금이 완료 되었습니다. 잔액은 {}원 입니다. 수수료는 {}원 입니다.".format(30000,balance,commision))


# 미리 초기값을 지정해 둘수도 있다.
def profile(name, age=17, subject="파이썬"):
    print("이름: {}, 나이: {}, 배우는 과목: {}".format(name,age,subject))

profile("이선민")
profile("민민",24,"자바")