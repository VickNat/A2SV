n, a, b = list(map(int, input().split()))
stud = list(map(int, input().split()))
 
left = 0
bCounts = 0
bTotal = 0
aTotal = 0
aCounts = 0
 
for right in range(n):
    bTotal += stud[right]
 
    while bTotal > b and left < right:
        bTotal -= stud[left]
        left += 1
 
    if bTotal <= b:
        bCounts += right - left + 1
    
left = 0
 
for right in range(0, n):
    aTotal += stud[right]    
    
    while aTotal >= a and left < right:
        aTotal -= stud[left]
        left += 1
 
    if aTotal < a:
        aCounts += right - left + 1
 
print(bCounts-aCounts)
