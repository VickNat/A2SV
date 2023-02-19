n, k = list(map(int, input().split()))
 
arr = sorted(list(map(int, input().split())))
 
ans = -1
 
if k != 0 and k < n and arr[k] != arr[k-1]:
    for i in range(arr[k-1] + 1, arr[k-1]-1, -1):
        if i not in arr or (i in arr and i == arr[k-1]):
            ans = i
            break
        
elif k == 0 and arr[0] != 1:
    ans = arr[0] - 1
elif k == n:
    ans = arr[k-1]
    
print(ans)
