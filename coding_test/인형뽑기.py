
def solution(board, moves):
    stack=[]
    answer = 0
    for locate in moves:
        idx=0
        for lst in board:
            if lst[locate-1]!=0:
                if stack and stack[-1]==lst[locate-1]:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(lst[locate-1])
                board[idx][locate-1]=0
                break
            idx+=1
    return answer


board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
move=[1,5,3,5,1,2,1,4]
print(solution(board, move))