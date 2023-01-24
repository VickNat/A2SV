testCases = int(input())

for i in range(testCases):
  size = int(input())
  array = list(map(int, input().split()))

  array.sort()

  idx = 0 
  while len(array) > 1:
    if array[idx+1] - array[idx] <= 1:
        array.remove(array[idx])
    else:
        break

  if len(array) == 1:
    print("YES")
  else:
    print("NO")
