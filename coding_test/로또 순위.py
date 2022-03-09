def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    zero=lottos.count(0)
    correct_num=0
    for num in lottos:
        if num in win_nums:
            correct_num+=1
    top=rank[zero+correct_num]
    low=rank[correct_num]
    answer = [top,low]
    return answer


lottos=[44, 1, 0, 0, 31, 25]
win_nums=[31, 10, 45, 1, 6, 19]
print(solution(lottos,win_nums))