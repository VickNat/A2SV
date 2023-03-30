'''
list(map(int, input().split()))
int(input())
'''

t = int(input())

for _ in range(t):
  num = int(input())
  val = 1
  andVal = 1

  while val <= num:
    if val&num != 0:
      andVal = val
      break

    val <<= 1

  xOr = 1

  if num == 1:
    xOr = 3
    
  if andVal ^ num > 0:
    print(andVal)
  else:
    print(xOr | andVal)