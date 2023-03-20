'''
list(map(int, input().split()))
int(input())
'''

t = int(input())

for _ in range(t):
    n, h = list(map(int, input().split()))
    attack = list(map(int, input().split()))
    
    l = 0
    r = h
    
    while l+1 < r:
        mid = l + (r-l)//2
        
        sum_ = 0
        for i in range(n-1):
            sum_ += min(mid, attack[i+1] - attack[i])
        sum_ += mid
        
        if sum_ >= h:
            r = mid
        else:
            l = mid
    
    print(r)
