class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        starts = []

        for idx in range(len(intervals)):
            starts.append([intervals[idx][0], idx])
        
        starts.sort()

        for elm in intervals:
            left = -1
            right = len(intervals)

            while left+1 < right:
                mid = left + (right-left)//2

                if starts[mid][0] >= elm[1]:
                    right = mid
                else:
                    left = mid
            
            if right == len(intervals):
                ans.append(-1)
            else:
                ans.append(starts[right][1])
        
        return ans