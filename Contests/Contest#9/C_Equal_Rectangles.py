'''
list(map(int, input().split()))
int(input())
'''

q = int(input())

for _ in range(q):
    n = int(input())
    rect = list(map(int, input().split()))
    size = len(rect)
    rect.sort()
    
    l = 0
    r = size-1
    check = 0
    ans = "YES"
    
    while l < r:
        if rect[r-1] == rect[r] and rect[l+1] == rect[l]:
            area = rect[r]*rect[l]
            
            if not check:
                check = area
            elif check != area:
                ans = "NO"
                break
            else:
                l += 2
                r -= 2
        else:
            ans = "NO"
            break
    
    print(ans)
                
