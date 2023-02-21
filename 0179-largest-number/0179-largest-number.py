class Solution:
    def comparator(self, a: str, b: str):
        comp = 0
        
        if a + b > b + a:
            comp -= 1
        elif a + b < b + a:
            comp += 1
        
        return comp
    
    def largestNumber(self, nums: List[int]) -> str:
        numsList = []
        
        for i in range(len(nums)):
            numsList.append(str(nums[i]))
            
        ans = sorted(numsList, key = cmp_to_key(self.comparator))
        
        ans = str(int("".join(ans)))
        return ans

                
                
                