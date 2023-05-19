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
  n = str(input())
  m = str(input())
  n = list(n)
  
  n = [int(i) for i in n]
  n.sort()
  ptr = 0
  while ptr < len(n) and n[ptr] == 0:
    ptr += 1
  
  if ptr < len(n):
    n[0], n[ptr] = n[ptr], n[0]
    
  n = [str(i) for i in n]
  n = "".join(n)

  if n == m:
    print("OK")
  else:
    print("WRONG_ANSWER")

main()