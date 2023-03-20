n, m = list(map(int, input().split()))
 
prefixSum = [0]*(n+1)
for _ in range(m):
    a, b = list(map(int, input().split()))
    prefixSum[a] += 1
    prefixSum[b+1] -= 1
 
pre = 0
for i in range(n):
    pre += prefixSum[i]
    prefixSum[i] = pre
    
ans = "NO"
for i in range(0, n):
    if prefixSum[i] <= 0:
        ans = "YES"
        break
 
print(ans)
