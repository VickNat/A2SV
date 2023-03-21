t = int(input())
 
for _ in range(t):
    a, b = list(map(int, input().split()))
    counts = 0
    check = (a+b)//4
    counts = min(a, b)
    
    print(min(counts, check))