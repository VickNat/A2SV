# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()

        left = 0
        right = N-1
        while left <= right:
            mid = (left+right)//2

            cur = mountain_arr.get(mid)
                
            if mid+1 < N and mountain_arr.get(mid) <= mountain_arr.get(mid+1):
                left = mid+1
            else:
                right = mid-1
        
        peak = left
        left = 0
        right = peak
        while left <= right:
            mid = (left+right)//2

            cur = mountain_arr.get(mid)
            if cur > target:
                right = mid-1
            else:
                left = mid+1
        
            if cur == target:
                return mid
        
        left = peak
        right = N-1
        while left <= right:
            mid = (left+right)//2

            cur = mountain_arr.get(mid)
            if cur >= target:
                left = mid+1
            else:
                right = mid-1
        
            if cur == target:
                return mid
        
        return -1