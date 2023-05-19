import math
from collections import defaultdict
from collections import Counter
from collections import deque

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  cols = InputInt()
  rows = 2
  graph = [[] for r in range(rows)]
  visited = set()
  directions = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

  for r in range(rows):
    row = list(input())
    graph[r] = row[:]

  def inbound(r, c):
    return 0 <= r < rows and 0 <= c < cols
  
  def dfs(r, c):
    if r == 1 and c == cols-1:
      return True
    
    visited.add((r, c))
    
    for changeR, changeC in directions:
      newR = r + changeR
      newC = c + changeC

      if inbound(newR, newC) and (newR, newC) not in visited and graph[newR][newC] == "0":
        val = dfs(newR, newC)
        if val:
          return True
    
    return False
  
  val = dfs(0, 0)
  if val:
    print("YES")
  else:
    print("NO")


T = InputInt()
for r in range(T):
  main()
    