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
  rows, cols = InputIterables()
  colors = set()
  graph = []
  visited = set()
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  for _ in range(rows):
    row = InpStrToList()
    colors = colors.union(set(row[:]))
    graph.append(row)
  
  def inbound(r, c):
    return 0 <= r < rows and 0 <= c < cols

  def bfs(pr, pc, p):
    queue = deque()
    queue.append((pr, pc, None, None))
    visited.add((pr, pc))

    while queue:
      r, c, parentR, parentC = queue.popleft()

      for changeR, changeC in directions:
        newR = r + changeR
        newC = c + changeC

        if (parentR, parentC) != (newR, newC) and inbound(newR, newC) and graph[newR][newC] == p:
          if (newR, newC) in visited:
            return True
          
          visited.add((newR, newC))
          queue.append((newR, newC, r, c))
            
  for r in range(rows):
    for c in range(cols):

      if (r, c) not in visited:
        if bfs(r, c, graph[r][c]):
          return True
  
ans = main()
if ans:
  print("Yes")
else:
  print("No")