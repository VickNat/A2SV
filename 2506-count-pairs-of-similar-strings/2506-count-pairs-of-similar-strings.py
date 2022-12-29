class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counts = 0
        
        for word1 in range(len(words)):
            for word2 in range(word1):
                
                if set(words[word1]) == set(words[word2]):
                    counts+=1
                   
        return counts