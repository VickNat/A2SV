n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
lessThanArr = []

ptr1 = 0
ptr2 = 0

# counts = 0

for ptr2 in range(m):
  if arr1[0] >= arr2[ptr2]:
    lessThanArr.append(0)
    continue

  while ptr1 < n and arr1[ptr1] < arr2[ptr2]:
    ptr1 += 1
    
  lessThanArr.append(ptr1)
  
print(*lessThanArr)
