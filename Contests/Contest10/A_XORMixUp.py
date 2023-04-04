'''
list(map(int, input().split()))
int(input())
'''

t = int(input())

for _ in range(t):
  N = int(input())
  nums = list(map(int, input().split()))
  ans = 0

  for i in range(N):
    val = 0

    for j in range(N):
      if i == j:
        continue
      val ^= nums[j]
    
    if val == nums[i]:
      ans = nums[i]
      break
  
