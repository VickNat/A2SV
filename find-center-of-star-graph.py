class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0][0]
        sec = edges[0][1]

        if first in edges[1]:
            return first
        return sec