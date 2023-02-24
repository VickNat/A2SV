class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        asciiVal = []
        length = len(s)
        prefixSum = [0]*length
            
        for idx in range(length):
            asciiVal.append(ord(s[idx]))
        
        for shift in shifts:
            l = shift[0]
            r = shift[1]
            direct = 1
            
            if shift[2] == 0:
                direct = -1
            prefixSum[l] += direct
            if r + 1 < length:
                prefixSum[r+1] -= direct
        
        prefixSum = list(accumulate(prefixSum))
                
        for idx in range(length):
            asciiVal[idx] += prefixSum[idx]%26
            
            if asciiVal[idx] >= 123:
                asciiVal[idx] -= 26
            
            asciiVal[idx] = chr(asciiVal[idx])
        
        return "".join(asciiVal)
        