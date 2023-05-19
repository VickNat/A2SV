import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
    N = InputInt()
    sequence = InputList()
    ans = sequence[0]

    for idx in range(1, N):
      ans &= sequence[idx]

    print(ans)

T = InputInt()
for _ in range(T):
  main()