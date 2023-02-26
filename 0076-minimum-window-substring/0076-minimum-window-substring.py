class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sLength = len(s)
        tDict = defaultdict(int)
        sDict = defaultdict(int)
        right = 0
        left = 0
        ans = []
        
        for let in t:
            tDict[let] += 1
                
        for right in range(sLength):
            if s[right] in tDict:
                sDict[s[right]] += 1
            
            while left < sLength:
                flag = True
                
                for idx in tDict:
                    if sDict[idx] < tDict[idx]:
                        flag = False
                        break
                
                if flag == True:
                    temp = []
                    temp.append(left)
                    temp.append(right)
                    
                    if len(ans) == 0:
                        ans.append(temp)
                    elif (ans[-1][1] - ans[-1][0]) + 1 > right - left + 1:
                        ans.append(temp)
                    
                    if s[left] in sDict:
                        sDict[s[left]] -= 1
                            
                    left += 1
                else:
                    break
                
        if len(ans) == 0:
            return ""
        else:
            return s[ans[-1][0] : ans[-1][1]+1]
            
            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        