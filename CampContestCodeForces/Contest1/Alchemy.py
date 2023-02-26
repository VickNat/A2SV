n = int(input())

arr = list(map(int, input().split()))

edPtr = 0
alpPtr = n-1
alpSum = 0
edSum = 0
alp = 0
ed = 0

while edPtr <= alpPtr:
    if alpSum == edSum:
        edSum += arr[edPtr]
        ed += 1
        edPtr += 1
    elif alpSum < edSum:
        alpSum += arr[alpPtr]
        alp += 1
        alpPtr -= 1
    elif edSum < alpSum:
        edSum += arr[edPtr]
        ed += 1
        edPtr += 1

print(ed, alp, end=" ")
    
