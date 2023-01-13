class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        unordered = 0
        
        for letter in range(len(strs[0])):
            for string in range(len(strs)):
                let = strs[string][letter]
                
                if string + 1 < len(strs) and let > strs[string+1][letter]:
                    unordered += 1
                    break
                
        return unordered