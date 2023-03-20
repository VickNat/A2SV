from collections import defaultdict
 
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
 
seg = defaultdict(int)
maxLen = [1, 1]
l = 0
 
for r in range(n):
    seg[arr[r]] += 1
    while len(seg) > k:
        seg[arr[l]] -= 1
        if seg[arr[l]] == 0:
            del seg[arr[l]]
        
        l += 1
    
    if maxLen[1]-maxLen[0]+1 < (r+1)-(l+1)+1:
        maxLen = [l+1, r+1]
  
print(*maxLen)
