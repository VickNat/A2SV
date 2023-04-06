'''
list(map(int, input().split()))
int(input())
'''

from collections import defaultdict

N = int(input())
sources = defaultdict(int)
sinks = defaultdict(int)

for r in range(N):
  row = list(map(int, input().split()))
  sum_ = sum(row)
  sources[r+1] += sum_

  for c in range(N):
    sinks[c+1] += row[c]

source = [elm for elm in sinks if sinks[elm] == 0]
sink = [elm for elm in sources if sources[elm] == 0]

print(len(source), *source)
print(len(sink), *sink)