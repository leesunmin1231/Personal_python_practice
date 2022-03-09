# 1~20까지 한명 치킨 3명 커피
'''
from random import *
lst=[]
for i in range (20):
    lst.append(i+1)
shuffle(lst)
chicken=sample(lst,1)
set(lst)
lst.remove(chicken[0])
coffee=sample(lst,3)
print("당첨자\n치킨:%s\n커피:%s %s %s\n축하드립니다!!"%(chicken[0],coffee[0],coffee[1],coffee[2]))
'''

from random import *
lst=range(1,21)
lst=list(lst)
shuffle(lst)
winners=sample(lst,4)
print("당첨자\n치킨:{}\n커피:{}\n축하드립니다!!".format(winners[0],winners[1:]))


