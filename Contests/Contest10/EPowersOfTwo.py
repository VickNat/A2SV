'''
list(map(int, input().split()))
int(input())
'''

N, K = list(map(int, input().split()))

if K > N:
  print("NO")
else:
  ans = []
  
  for idx in range(32):
    if N & (1<<idx):
      ans.append(1<<idx)

  i = 0

  while len(ans) < K:
    while ans[i] == 1:
      i += 1
    
    ans[i] //= 2
    ans.append(ans[i])
    
  if len(ans) == K:
    print("YES")
    print(*sorted(ans))
  else:
    print("NO")
