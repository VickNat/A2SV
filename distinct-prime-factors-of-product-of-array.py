class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()

        for elm in nums:
            d = 2

            while d*d <= elm:
                while elm%d == 0:
                    ans.add(d)
                    elm //= d
                
                d += 1
            
            if elm > 1:
                ans.add(elm)
        
        return len(ans)