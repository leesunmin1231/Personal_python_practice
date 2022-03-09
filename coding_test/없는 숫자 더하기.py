'''
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 수 ≤ 9
numbers의 모든 수는 서로 다릅니다.
'''
def solution(numbers):
    sum=0
    for i in range(10):
        if i in numbers:
            continue
        else:
            sum+=i
    return sum

numbers=[5,8,4,0,6,7,9]
result=solution(numbers)
print(result)