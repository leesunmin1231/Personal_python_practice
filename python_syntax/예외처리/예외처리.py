class bignumbererror(Exception):
    pass
try:
    print("한자리 숫자 나누기 전용 계산기 입니다.")
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("두 번째 숫자를 입력하세요 : "))
    result=num1/num2
    if num1>=10 or num2>=10:
        raise bignumbererror
    print("{} 나누기 {}는 {}입니다.".format(num1,num2))
except ValueError:  # 위에서 ValueError 가 발생하면 여기가 실행됨.
    print("잘못된 값을 입력하였습니다. 숫자로 입력하세요.")
except bignumbererror:
    print("한자리 숫자로 입력하세요.")

finally:
    print("계산기를 이용해 주셔서 감사합니다.")
    # try이 구문이 실행되던지, except 구문이 실행되던지 혹은 여기에 없는 새로운 에러가 발생하더라도
    # finally 구문은 반드시 실행된다.
