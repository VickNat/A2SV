from collections import defaultdict

testCases = int(input())

for tests in range(testCases):
    nums = input()
    size = len(nums)
    
    left = 0
    right = 0
    counts = float('inf')
    numbers = defaultdict(int)
    
    while right < size:
        if nums[right] == "1":
            numbers["1"] += 1
        elif nums[right] == "2":
            numbers["2"] += 1
        else:
            numbers["3"] += 1
        
        right += 1
        
        while numbers["1"] > 0 and numbers["2"] > 0 and numbers["3"] > 0:
            counts = min(counts, right-left)

            if nums[left] == "1":
                numbers["1"] -= 1
            elif nums[left] == "2":
                numbers["2"] -= 1
            else:
                numbers["3"] -= 1
            
            left += 1
        
    
    if counts == float('inf'):
        counts = 0
        
    print(counts)
