class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        N = len(nums)
        counts = 0

        for i in range(N):
            for j in range(i, N):
                gcd = reduce(math.gcd, nums[i:j+1])

                if gcd == k:
                    counts += 1
                elif gcd != k and nums[j]%k != 0:
                    break
        
        return counts