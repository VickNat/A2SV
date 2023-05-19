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
  xo, yo, x1, y1 = InputIterables()
  N = InputInt()
  available = defaultdict(list)
  visited = set((xo, yo))
  queue = deque([(xo, yo)])
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
  rows = 10**9
  cols = 10**9
  levels = 0

  for _ in range(N):
    r, a, b = InputIterables()
    available[r].append((a, b))
  
  def inbound(r, c):
    return 0 <= r < rows and 0 <= c < cols

  while queue:
    size = len(queue)

    for _ in range(size):
      r, c = queue.popleft()
      if (r, c) == (x1, y1):
        return levels

      for changeR, changeC in directions:
        newR = r + changeR
        newC = c + changeC


        if inbound(newR, newC) and (newR, newC) not in visited:
          for val in available[newR]:
            if val[0] <= newC <= val[1]:
              queue.append((newR, newC))
              visited.add((newR, newC))
              break

    levels += 1
  return -1

print(main())
