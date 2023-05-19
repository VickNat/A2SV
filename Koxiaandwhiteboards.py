import math
from collections import defaultdict
from collections import Counter
from collections import deque
import heapq

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))
def InpStrToList(): return list(input())

def main():
  N, M = InputIterables()
  n_nums = InputList()
  m_nums = InputList()

  heapq.heapify(n_nums)
  
  for num in m_nums:
    heapq.heappop(n_nums)
    heapq.heappush(n_nums, num)
  
  print(sum(n_nums))

T = InputInt()
for _ in range(T):
  main()


