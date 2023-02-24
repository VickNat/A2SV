size = int(input())
nums = list(map(int, input().split()))
counts = 0
check = []
 
for elm in nums:
    if elm == 1 or elm == -1:
        check.append(elm)
    elif elm < -1:
        check.append(-1)
        counts += abs(elm + 1)
    elif elm > 1:
        check.append(1)
        counts += elm - 1
    elif elm == 0:
        check.append(1)
        counts += 1
 
prod = 1
for idx in check:
    prod *= idx
    
 
if prod < 0:
    if 0 not in nums:
        counts += 2
 
    
    
print(counts)
