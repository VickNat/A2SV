'''
list(map(int, input().split()))
int(input())
'''

num = int(input())
counts = 0

while num > 1:
  bact = 2
  while bact <= num:
    bact *= 2

  if bact > num:
    bact //= 2
  
  num -= bact
  counts += 1

if num == 1:
  counts += 1

print(counts)
