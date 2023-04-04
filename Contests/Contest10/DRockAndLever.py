'''
list(map(int, input().split()))
int(input())
'''

from collections import defaultdict

def lastBitCounter(num):
  last = 0
  while num:
    num >>= 1
    last += 1
  return last

t = int(input())

for _ in range(t):
  N = int(input())
  nums = list(map(int, input().split()))
  lastBits = defaultdict(int)
  counts = 0

  for idx in range(N):
    elm = nums[idx]
    last = lastBitCounter(elm)

    counts += lastBits[last]
    
    lastBits[last] += 1
  
  print(counts)
