import math
from collections import defaultdict
from collections import Counter
from collections import deque

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))
def InpStrToList(): return list(input())

def main():
  rows, cols, p = InputIterables()
  maze = []
  mouse = []
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  visited = set()
  queue = deque()

  for _ in range(rows):
    r = InpStrToList()
    maze.append(r)

    if 'M' in r:
      c = r.index('M')
      mouse = [_, c]
  
  moves = InputList()
  maze[mouse[0]][mouse[1]] = "."

  for elm in moves:
    if elm == 1:
      mouse[0] -= 1
    elif elm == 2:
      mouse[0] += 1
    elif elm == 3:
      mouse[1] -= 1
    elif elm == 4:
      mouse[1] += 1
  
  queue.append((mouse[0], mouse[1]))
  levels = 0
  
  def inbound(r, c):
    return 0 <= r < rows and 0 <= c < cols and maze[r][c] != "#"
  
  while queue and levels < p:
    N = len(queue)

    for _ in range(N):
      r, c = queue.popleft()

      for changeR, changeC in directions:
        newR = r + changeR
        newC = c + changeC

        if inbound(newR, newC) and (newR, newC) not in visited:
          visited.add((newR, newC))
          queue.append((newR, newC))
    
    levels += 1
  
  print(len(visited))

main()

    