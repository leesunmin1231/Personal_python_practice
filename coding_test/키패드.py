'''
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 
두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 
오른손잡이는 오른손 엄지손가락, 
왼손잡이는 왼손 엄지손가락을 사용합니다.
'''
def solution(numbers, hand):
    phone_num=[[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    left_thumb=[0,3]
    right_thumb=[2,3]
    answer = ''
    for num in numbers:
        if num in phone_num[0]:
            answer+="L"
            left_thumb=[0,num//3]
        elif num in phone_num[2]:
            right_thumb=[2,num//3-1]
            answer+="R"
        else:
            if num==0:
                num_idx=3
            else:
                num_idx=num//3
            L_distance=(1-left_thumb[0])+abs(left_thumb[1]-num_idx)
            R_distance=(right_thumb[0]-1)+abs(right_thumb[1]-num_idx)
            if L_distance > R_distance:
                answer+="R"
                right_thumb=[1,num_idx]
            elif L_distance < R_distance:
                answer+="L"
                left_thumb=[1,num_idx]
            else:
                if hand == "left":
                    answer+="L"
                    left_thumb=[1,num_idx]
                else:
                    answer+="R"
                    right_thumb=[1,num_idx]
    return answer

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"
print(solution(numbers, hand))
# LRLLLRLLLRL 내답
# LRLLLRLLRRL