class Solution:
    def frequency(self, s):
        ans = list(s)
        ans.sort()
        left = -1
        right = len(ans)
        checker = ans[0]

        while left+1 < right:
            mid = left + (right-left)//2

            if ans[mid] > checker:
                right = mid
            else:
                left = mid

        return right 
            

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freq = [0]*len(queries)

        for idx in range(len(queries)):
            elm = queries[idx]
            queries[idx] = self.frequency(elm)

        for idx in range(len(words)):
            elm = words[idx]
            words[idx] = self.frequency(elm)
            
        words.sort()
        
        for idx in range(len(queries)):
            elm = queries[idx]
            left = -1
            right = len(words)

            while left+1 < right:
                mid = left + (right-left)//2

                if elm >= words[mid]:
                    left = mid
                else:
                    right = mid
            
            freq[idx] = len(words)-right
        
        return freq