class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        right = size
        left = -1

        while left+1 < right:
            mid = left + (right-left)//2
            index = size-mid

            if index > citations[mid]:
                left = mid
            else:
                right = mid
        
        return size-right