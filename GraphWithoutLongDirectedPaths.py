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
  n, m = InputIterables()
  graph = defaultdict(list)
  colors = defaultdict(int)
  edges = []
  queue = deque([1])
  colors[1] = 1
  flag = True

  for _ in range(m):
    a, b = InputList()
    edges.append([a, b])
    graph[a].append(b)
    graph[b].append(a)
  
  while queue:
    cur = queue.popleft()

    for elm in graph[cur]:
      if not colors[elm]:
        colors[elm] = 3 - colors[cur]

        queue.append(elm)
      elif colors[elm] == colors[cur]:
        flag = False
        break
    
    if not flag:
      break

  ans = "NO"
  string = []
  if flag:
    ans = "YES"

    for a, b in edges:
      if colors[a] < colors[b]:
        string.append("0")
      else:
        string.append("1")

  print(ans)
  if string:
    print("".join(string))
main()