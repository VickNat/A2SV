class Solution:
    def binaryConverter(self, n):
        if n == 1:
            return "0"
        
        ans = self.binaryConverter(n-1)
        inverted = ""

        for idx in range(len(ans)):
            if ans[idx] == "0":
                inverted += "1"
            else:
                inverted += "0"
        
        reversed_string = inverted[::-1]
        ans += "1" + reversed_string
        
        return ans

    def findKthBit(self, n: int, k: int) -> str:
        binary_string = self.binaryConverter(n)
        return binary_string[k-1]