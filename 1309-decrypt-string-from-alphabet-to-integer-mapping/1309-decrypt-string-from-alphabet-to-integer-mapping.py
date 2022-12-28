class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted_str = []
        idx=0
        
        while idx < len(s):
            if idx+2<len(s) and s[idx+2] == "#":
                temp = int(s[idx:idx+2])
                temp += 96
                decrypted_str.append(chr(temp))
                idx+=3
            else:
                asci = int(s[idx]) + 96
                decrypted_str.append(chr(asci))
                idx+=1
            
        
        return "".join(decrypted_str)