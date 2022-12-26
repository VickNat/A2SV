class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        pref_str = strs[0]
        
        for str_idx in strs:
            for index in range(0, len(pref_str)):
                if index >= len(str_idx) or pref_str[index] != str_idx[index]:
                    pref_str = pref_str[0:index]
                    break
                    
        return pref_str