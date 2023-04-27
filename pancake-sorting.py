class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)

        while n > 0:
            k = arr.index(n)
            
            if k != n-1:
                if k != 0:
                    flips.append(k+1)
                    arr[:k+1] = reversed(arr[:k+1])

                k = n
                flips.append(k)
                arr[:k] = reversed(arr[:k])
            n -= 1

        return flips