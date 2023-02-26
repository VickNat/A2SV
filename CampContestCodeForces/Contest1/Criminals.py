t = int(input())

for _ in range(t):
    n = int(input())
    criminals = list(map(int, input().split()))
    
    total = sum(criminals)
    total -= criminals[-1]
    counts = total
    l = 0
    
    for r in range(1, n-1):
        while criminals[l] == 0 and l<r:
            l += 1
        
        if criminals[r] == 0 and criminals[l] != 0:
            counts += 1
        
    print(counts)
