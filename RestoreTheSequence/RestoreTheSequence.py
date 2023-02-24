testCases = int(input())
 
for tests in range(testCases):
    size = int(input())
    nums = list(map(int, input().split()))
    
    left = 0
    right = size - 1
    ans = []
    
    while left < right:
        ans.append(nums[left])
        ans.append(nums[right])
        
        left += 1
        right -= 1
    
    if size%2 != 0:
        ans.append(nums[left])
    
    print(*ans)
