class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)

        @cache
        def dp(i, j):
            ans = 1
            max_ = 0
            
            for idx1 in range(i+1, N):
                for idx2 in range(j+1, M):
                    if nums1[idx1] == nums2[idx2]:
                        max_ = max(max_, dp(idx1, idx2))
            
            return ans+max_
        
        ans = 0

        for i in range(N):
            for j in range(M):
                if nums1[i] == nums2[j]:
                    ans = max(ans, dp(i, j))
        
        return ans