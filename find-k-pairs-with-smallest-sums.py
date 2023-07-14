class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        size1 = len(nums1)
        size2 = len(nums2)
        heap = []
        heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited = set()
        ans = []

        while heap and len(ans) < k:
            sum_, idx1, idx2 = heappop(heap)
            ans.append((nums1[idx1], nums2[idx2]))
            print(idx1, idx2)

            if idx1+1 < size1 and (idx1+1, idx2) not in visited:
                heappush(heap, (nums1[idx1+1]+nums2[idx2], idx1+1, idx2))
                visited.add((idx1+1, idx2))
            if idx2+1 < size2 and (idx1, idx2+1) not in visited:
                heappush(heap, (nums1[idx1]+nums2[idx2+1], idx1, idx2+1))
                visited.add((idx1, idx2+1))
        
        return ans