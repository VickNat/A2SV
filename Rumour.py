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
  heap = InputList()
  graph = defaultdict(list)
  visited = set()
  ans = 0
  

  for _ in range(M):
    first, second = InputIterables()
    graph[first].append(second)
    graph[second].append(first)
  
  for i in range(N):
    heap[i] = [heap[i], i+1]
  
  heapq.heapify(heap)

  def bfs(p):
    queue = deque()
    queue.append(p)
    
    while queue:
      val = queue.popleft()

      for elm in graph[val]:
        if elm not in visited:
          queue.append(elm)
          visited.add(elm)
  
  while heap:
    cost, p = heapq.heappop(heap)

    if p not in visited:
      bfs(p)
      ans += cost
  
  print(ans)

main()