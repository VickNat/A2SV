t = int(input())
 
for _ in range(t):
    n, m = list(map(int, input().split()))
    divider = list(map(int, input().split()))
    divider.sort(reverse=True)
    
    ptr = 0
    counts = 0
    outlets = 2
    
    if n <= outlets:
        print(0)
    else:
        while ptr < m:
            outlets += divider[ptr] - 1
            counts += 1
            
            if outlets >= n:
                break
            
            ptr += 1
        
        if outlets >= n:
            print(counts)
        else:
            print(-1)
