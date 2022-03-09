def find(data,count):
    if data%2==0:
        return count
    else:
        i=1
        while (2*i+1)<data:
            if data%(2*i+1)==0:
                return count
            else:
                i+=1
                continue
        count+=1
        return count
        
def solution(nums):
    count=0
    n1=0
    n2=1
    n3=2
    loop=(len(nums)*(len(nums)-1)*(len(nums)-2))/6
    for i in range(int(loop)):
        data=nums[n1]+nums[n2]+nums[n3]
        count=find(data,count)
        if n1==len(nums)-3:
            break
        elif n2==len(nums)-2:
            n1+=1
            n2=n1+1
            n3=n2+1
            continue
        else:
            if n3==len(nums)-1:
                n2+=1
                n3=n2+1
                continue
            else:
                n3+=1
                continue
    return count

lst1=[1,2,7,6,3,34,75,3,98,4]
d=solution(lst1)
print(d)