from collections import defaultdict
 
size = list(map(int, input().split()))
n = size[0]
m = size[1]
 
words = []
 
for _ in range(n):
    temp = list(input())
    
    words.append(temp)
    
duplicates = set()
 
 
for r in range(n):
    letters = defaultdict(list)
    
    for c in range(m):
        temp = [r, c]
        
        if words[r][c] not in letters:
            letters[words[r][c]] = temp
        else:
            duplicates.add(tuple(letters[words[r][c]]))
            duplicates.add(tuple(temp))
 
for c in range(m):
    letters = defaultdict()
    
    for r in range(n):
        temp = [r, c]
        
        if words[r][c] not in letters:
            letters[words[r][c]] = temp
            
        else:
            duplicates.add(tuple(letters[words[r][c]]))
            duplicates.add(tuple(temp))
 
 
ans = ""
 
for r in range(n):
    for c in range(m):
        temp = [r, c]
        if tuple(temp) not in duplicates:
            ans += words[r][c]
 
print(ans)
