'''
list(map(int, input().split()))
int(input())
'''

l, r = list(map(int, input().split()))
val = l^r
ans = 0

while val > 0:
  ans |= 1
  ans <<= 1
  val >>= 1

print(ans//2)
