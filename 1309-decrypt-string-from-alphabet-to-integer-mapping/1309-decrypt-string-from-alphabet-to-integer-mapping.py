class Solution:
    def freqAlphabets(self, s: str) -> str:
        ptr = len(s)-1
        answer = []
        
        while ptr >= 0:
            letter = ""
            
            if s[ptr] == "#":
                letter = int(s[ptr-2:ptr]) + 96
                
                ptr-=3
            else:
                letter = int(s[ptr]) + 96
                
                ptr-=1
            
            answer.append(chr(letter))
        
        answer.reverse()
        
        return "".join(answer)

        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         decrypted_str = []
#         idx=0
        
#         while idx < len(s):
#             if idx+2<len(s) and s[idx+2] == "#":
#                 temp = int(s[idx:idx+2])
#                 temp += 96
#                 decrypted_str.append(chr(temp))
#                 idx+=3
#             else:
#                 asci = int(s[idx]) + 96
#                 decrypted_str.append(chr(asci))
#                 idx+=1
            
        
#         return "".join(decrypted_str)