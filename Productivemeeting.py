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
  N = InputInt()
  minHeap = InputList()
  ans = []

  for idx in range(N):
    minHeap[idx] = [-minHeap[idx], idx+1]
  
  heapq.heapify(minHeap)
  
  while len(minHeap) > 1:
    val1, idx1 = heapq.heappop(minHeap)
    val2, idx2 = heapq.heappop(minHeap)

    val1 = abs(val1)
    val2 = abs(val2)
    if val1 and val2:
      val1 -= 1
      val2 -= 1
      ans.append([idx2, idx1])

      if val1 > 0:
        heapq.heappush(minHeap, [-val1, idx1])
      if val2 > 0:
        heapq.heappush(minHeap, [-val2, idx2])
    elif not val2 and val1:
      heapq.heappush(minHeap, [-val1, idx1])
    elif not val1 and val2:
      heapq.heappush(minHeap, [-val2, idx2])

  print(len(ans))
  if ans:
    ans.sort()
    for elm in ans:
      print(*(elm))
      
T = InputInt()
for _ in range(T):
  main()