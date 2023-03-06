class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        subArr = float('inf')
        size = len(nums)
        queue = deque()
        prefixSum = list(accumulate(nums, initial = 0))
        
        for idx, value in enumerate(prefixSum):
            while queue and value - prefixSum[queue[0]] >= k:
                subArr = min(subArr, idx-queue[0])
                queue.popleft()

            while queue and prefixSum[queue[-1]] > value:
                queue.pop()
            queue.append(idx)            
        
        if subArr == float('inf'):
            return -1
        return subArr