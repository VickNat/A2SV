b = int(input())
boys = list(map(int, input().split()))
 
g = int(input())
girls = list(map(int, input().split()))
 
boys.sort()
girls.sort()
 
bPtr = 0
gPtr = 0
pairs = 0
 
while bPtr < b and gPtr < g:
    if abs(girls[gPtr] - boys[bPtr]) <= 1:
        pairs += 1
        bPtr += 1
        gPtr += 1
    elif girls[gPtr] > boys[bPtr]:
        bPtr += 1
    else:
        gPtr += 1
 
print(pairs)
