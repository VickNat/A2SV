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
  l, r = InputIterables()

  if l == 1:
    print(l, r)
  else:
    if r%2 != 0:
      r -= 1
    
    print(r//2, r)

T = InputInt()
for _ in range(T):
  main()