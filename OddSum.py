n = int(input())
 
size = 2*n
 
array = list(map(int, input().split()))
 
array.sort()
 
right = size - 1
left = 0
rSum = 0
lSum = 0
 
while left < right:
    rSum += array[right]
    lSum += array[left]
    
    right -= 1
    left += 1
 
if rSum != lSum:
    print(*array)
else:
    print(-1)
