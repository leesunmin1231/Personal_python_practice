'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
'''
def solution(answers):
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx in range(len(answers)):
        if answers[idx] == arr1[idx%len(arr1)]:
            score[0] += 1
        if answers[idx] == arr2[idx%len(arr2)]:
            score[1] += 1
        if answers[idx] == arr3[idx%len(arr3)]:
            score[2] += 1

    for i in range(len(score)):
        if score[i] == max(score):
            result.append(i+1)

    return result


ans=[5,4,4,2,2,5,3]
a=solution(ans)
print(a)

