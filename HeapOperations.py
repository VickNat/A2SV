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
  heap = []
  insert = "insert"
  removeMin = "removeMin"
  getMin = "getMin"
  ans = []

  for _ in range(N):
    op = list(input().split(" "))

    if op[0] == insert:
      heapq.heappush(heap, int(op[1]))
      ans.append(insert + " " + str(op[1]))
    elif op[0] == removeMin:
      if not heap:
        heapq.heappush(heap, 0)
        ans.append(insert + " " + str(0))

      heapq.heappop(heap)
      ans.append(removeMin)
    elif op[0] == getMin:
      while heap and heap[0] < int(op[1]):
        ans.append(removeMin)
        heapq.heappop(heap)
      
      if heap and heap[0] == int(op[1]):
        ans.append(getMin + " " + str(heap[0]))
      else:
        heapq.heappush(heap, int(op[1]))
        ans.append(insert + " " + str(op[1]))
        ans.append(getMin + " " + str(heap[0]))
  
  print(len(ans))
  for elm in ans:
    print(elm)

main()
