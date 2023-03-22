class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        def dfs(first, second, idx):
            if idx == n:
                return True
            
            if num[idx] == '0' and (second != 0 or first == 0):
                return False
            
            total = first + second
            total_str = str(total)
            total_len = len(total_str)
            
            if idx + total_len > n:
                return False
            
            if num[idx:idx+total_len] != total_str:
                return False
            
            return dfs(second, total, idx+total_len)
        
        for i in range(1, n//2+1):
            if num[0] == '0' and i > 1:
                break
            first = int(num[:i])
            
            for j in range(i+1, n):
                if num[i] == '0' and j > i+1:
                    break
                second = int(num[i:j])

                if first == 0 and second == 0:
                    if j == n-1:
                        return True
                    else:
                        break
                
                if dfs(first, second, j):
                    return True
        
        return False