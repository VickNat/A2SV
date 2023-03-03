class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        ans = self.getRow(rowIndex-1)
        temp = [0]*(len(ans)+1)
        ptr = 1

        while ptr < len(ans):
            temp[ptr] = ans[ptr-1] + ans[ptr]
            ptr += 1
        
        temp[0] = 1
        temp[-1] = 1
        ans = temp

        return ans