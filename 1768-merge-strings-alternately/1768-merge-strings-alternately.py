class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        len1 = len(word1)
        len2 = len(word2)
        length = min(len1,len2)
        
        for index in range(length):
            merged += word1[index]
            merged += word2[index]
            
        if length == len1:
            merged += word2[length:]
        elif length == len2:
            merged += word1[length:]
            
        return merged