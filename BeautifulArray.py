n = int(input())
ar = list(map(int, input().split()))
 
zero = []
pos = []
neg = []
 
arr = sorted(ar)
 
neg.append(arr[0])
 
for idx in range(1, len(arr)):
    val = arr[idx]
    
    if val == 0:
        zero.append(val)
    elif val > 0:
        pos.append(val)
 
if len(pos) == 0:
    for i in range(1, 3):
        if arr[i] < 0:
            pos.append(arr[i])
 
for j in range(len(arr)):
    if arr[j] not in pos and arr[j] not in neg and arr[j] not in zero:
        zero.append(arr[j])
 
print(len(neg), *neg)
print(len(pos), *pos)
print(len(zero), *zero)
