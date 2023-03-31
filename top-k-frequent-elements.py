class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []

        def quickSort(arr):
            N = len(arr)

            if N < 2:
                if len(arr) == 1:
                    ans.append([arr[0], 1])
                return arr
            
            pivot = arr[N//2]

            left = [l for l in arr if l < pivot]
            mid = [m for m in arr if m == pivot]
            right = [r for r in arr if r > pivot]
            
            ans.append([pivot, len(mid)])
            
            return quickSort(left) + mid + quickSort(right)
        
        quickSort(nums)
        ans.sort(key=lambda x: x[1])
        freq = []

        idx = len(ans)-k
        while idx < len(ans):
            freq.append(ans[idx][0])
            idx += 1

        return freq