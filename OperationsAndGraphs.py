'''
list(map(int, input().split()))
int(input())
'''
from collections import defaultdict

n = int(input())
k = int(input())
graph = defaultdict(list)

for _ in range(k):
  oper = list(map(int, input().split()))

  if len(oper) == 2:
    print(*graph[oper[1]])
  else:
    u = oper[1]
    v = oper[2]

    graph[u].append(v)
    graph[v].append(u)