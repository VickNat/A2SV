'''
list(map(int, input().split()))
int(input())
'''

from collections import defaultdict

N = int(input())
adjecency_list = defaultdict(list)

for r in range(N):
  row = list(map(int, input().split()))

  for c in range(N):
    if row[c] == 1:
      adjecency_list[r+1].append(c+1)

for row in adjecency_list:
  print(len(adjecency_list[row]), *adjecency_list[row])
