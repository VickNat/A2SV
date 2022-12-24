# n can accept both n and m as a list after splitting
n = list(map(int, input().split()))

happyArr = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

counts = 0

for i in happyArr:
    if i in setA:
        counts += 1
    if i in setB:
        counts -= 1
        
print(counts)
