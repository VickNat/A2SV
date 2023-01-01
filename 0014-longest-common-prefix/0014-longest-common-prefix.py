class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        
        prefStr = strs[0]
        
        for word in strs:
            for index in range(0, len(prefStr)):
                if index>=len(word) or prefStr[index]!=word[index]:
                    prefStr = prefStr[:index]
                    break
            
        return prefStr