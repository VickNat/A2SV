n = int(input())
queue = list(map(str, input().split()))
q = int(input())
 
for _ in range(q):
    person = input()
    
    left = -1
    right = n
    
    while left+1 < right:
        mid = left + (right - left)//2
        
        if queue[mid] > person:
            right = mid
        elif queue[mid] < person:
            left = mid
        else:
            right = mid
            break
        
    print(right)
