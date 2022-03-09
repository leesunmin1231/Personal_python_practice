'''
time=10
def time_machine(freq,current_hour,current_min):
    global time # 함수내에서 전역 변수 이용하는 방식
    if current_min>=freq*time:
        after_hour=current_hour
        after_min=current_min-freq*time
    else:
        after_hour=current_hour-1
        after_min=(current_min+60)-freq*time
    return after_hour,after_min

hour,min=time_machine(5,13,50)
print(hour,":",min)
'''
# 또다른 방법
time=10
def time_machine(time,freq,current_hour,current_min):
    
    if current_min>=freq*time:
        after_hour=current_hour
        after_min=current_min-freq*time
    else:
        after_hour=current_hour-1
        after_min=(current_min+60)-freq*time
    return after_hour,after_min

hour,min=time_machine(time,5,11,30)
print(hour,":",min)
