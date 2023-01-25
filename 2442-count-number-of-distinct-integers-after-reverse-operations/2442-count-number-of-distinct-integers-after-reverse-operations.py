class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set(nums)
        # counts = len(check)
        
        for num in nums:
            temp = 0
            
            while num != 0:
                temp = (temp*10) + num%10
                    
                num //= 10
            
            ans.add(temp)
            
        # for elm in ans:
        #     if elm not in nums:
        #         counts += 1
        
        return len(ans)