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
  n, k = InputIterables()
  graph = defaultdict(list)
  queue = deque()
  levels = 0
  indegree = defaultdict(int)

  
  for _ in range(n-1):
    a, b = InputIterables()
    graph[a].append(b)
    graph[b].append(a)
    indegree[a] += 1
    indegree[b] += 1

  for key, val in indegree.items():
    if val == 1:
      queue.append(key)
  
  while queue:
    if levels == k:
      break

    size = len(queue)

    for _ in range(size):
      cur = queue.popleft()

      elm = graph[cur][0]
      indegree[elm] -= 1
      indegree[cur] -= 1

      if indegree[elm] == 1:
        queue.append(elm)
    
      del graph[cur]
    levels += 1

  return len(graph)

T = InputInt()
for _ in range(T):
  empty = input()
  print(main())