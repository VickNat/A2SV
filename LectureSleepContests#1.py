minutes, k = list(map(int, input().split()))
theory = list(map(int, input().split()))
sleep = list(map(int, input().split()))

wake = 0

for idx in range(minutes):
    if sleep[idx]==1:
        wake += theory[idx]
    
left = 0
right = 0
answer = 0

for index in range(minutes):
    total = wake
    
    while right<minutes:
        if sleep[right]==0:
            total+=theory[right]
        
        if right-left>=k:
            if sleep[left]==0:
                total-=theory[left]
                
            left+=1
        
        answer = max(answer, total)
        right+=1
        
        '''
        for tot in range(left, right + 1):
        if sleep[tot] == 0:
            total += theory[tot]

    answer = max(answer, total)
    left += 1
    right += 1'''
    
print(answer)
