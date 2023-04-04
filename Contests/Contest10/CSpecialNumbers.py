'''
list(map(int, input().split()))
int(input())
'''
t = int(input())

for _ in range(t):
  N, K = list(map(int, input().split()))
  counts = 0
  ans = 0
  while K:
    if K&1:
      ans += N**counts
    
    K >>= 1
    counts += 1

  print((ans)%((10**9)+7))
