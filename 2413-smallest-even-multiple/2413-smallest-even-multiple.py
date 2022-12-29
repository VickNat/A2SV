class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiple = 1
        
        while multiple%n!=0 or multiple%2!=0:
            multiple+=1
            
        return multiple
        