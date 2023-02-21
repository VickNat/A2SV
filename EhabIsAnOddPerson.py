n = int(input())
arr = list(map(int, input().split()))

ptr1 = 0
odd = 0
even = 0

while ptr1 < n:
    if arr[ptr1]%2 == 0:
        even += 1
    elif arr[ptr1]%2 != 0:
        odd += 1
    
    ptr1 += 1

if odd > 0 and even > 0:
    arr.sort()
    
print(*arr)
