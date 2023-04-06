import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

roads = 0

def main():
  global roads
  row = InputList()
  roads += sum(row)

N = int(input())
for r in range(N):
  main()

print(roads//2)