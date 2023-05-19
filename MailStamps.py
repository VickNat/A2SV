import math
from collections import defaultdict
from collections import Counter
from collections import deque

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  N = InputInt()
  graph = defaultdict(list)
  visited = set()
  stack = []
  ans = []

  for i in range(N):
    A, B = InputIterables()

    graph[A].append(B)
    graph[B].append(A)
    
  for key, val in graph.items():
    if len(val) == 1:
      visited.add(key)
      stack.append(key)
      break
    
  while stack:
    current = stack.pop()
    visited.add(current)
    ans.append(current)

    for child in graph[current]:
      if child not in visited:
        stack.append(child)
  
  print(*ans)

main()