class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = list(range(n))
        ans = []

        for source, sink in edges:
            sources[sink] = n+1
        
        for elm in sources:
            if elm < n:
                ans.append(elm)

        return ans