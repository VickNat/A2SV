class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        N = len(words)
        wordBits = []

        for word in words:
            num = 0

            for idx in range(len(word)):
                offset = ord(word[idx])-ord('a')
                num |= 1<<offset

            wordBits.append(num)
        
        for i in range(N-1):
            for j in range(i+1, N):
                num1 = wordBits[i]
                num2 = wordBits[j]

                if num1&num2 == 0:
                    ans = max(ans, len(words[i])*len(words[j]))

        return ans