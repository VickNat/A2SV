class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def traverse(row, idx, parity):
            if row == 1:
                if parity == "o":
                    return 0
                return 1
            
            tempIdx = ceil(idx/2)
            par = "e"

            if tempIdx%2 != 0:
                par = "o"
            
            cur = traverse(row-1, tempIdx, par)
            
            if cur == 0:
                if parity == "e":
                    return 1
                return 0
            
            if cur == 1:
                if parity == "e":
                    return 0
                return 1
        
        par = "e"
        if k%2 != 0:
            par = "o"

        return traverse(n, k, par)