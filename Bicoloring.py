import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

N = 0

def main():
  E = InputInt()
  edges = [[] for _ in range(N)]
  visited = [0]*N
  visited[0] = 1

  for _ in range(E):
    edge1, edge2 = InputList()
    edges[edge1-1].append(edge2)
    edges[edge2-1].append(edge1)
  
  def dfs():

    for idx, node in enumerate(edges):
      for elm in node:
        idx2 = elm-1

        if visited[idx] == visited[idx2]:
          return False
        
        if visited[idx2] == 0:
          visited[idx2] = 3-visited[idx]
        
    return True

  if dfs():
    print("BICOLOURABLE.")
  else:
    print("NOT BICOLOURABLE.")

while 1:
  N = InputInt()
  if N == 0: break

  main()