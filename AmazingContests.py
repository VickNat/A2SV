size = int(input())
 
contests = list(map(int, input().split()))
 
minScore = contests[0]
maxScore = contests[0]
counts = 0
idx = 1
 
 
 
for idx in range(len(contests)):
    if contests[idx]>maxScore:
        counts+=1
        maxScore = contests[idx]
    elif contests[idx]<minScore:
        counts+=1
        minScore = contests[idx]
    else:
        continue
 
print(counts)
