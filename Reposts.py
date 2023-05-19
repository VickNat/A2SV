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

  for _ in range(N):
    person1, repost, person2 = list(map(str, input().split(" ")))
    graph[person2.lower()].append(person1.lower())

  def dfs(person):
    
    visited.add(person)
    maxPath = 0

    for idx, elm in enumerate(graph[person]):
      if elm not in visited:
        maxPath = max(dfs(elm), maxPath)
    
    return maxPath + 1
  
  ans = dfs("polycarp")
  print(ans)

main()