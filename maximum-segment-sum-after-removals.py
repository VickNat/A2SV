class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N = len(nums)
        parent = [i for i in range(N)]
        size = [1 for i in range(N)]
        sum_ = [nums[i] for i in range(N)]
        ans = [0 for i in range(N)]
        check = [0 for i in range(N)]
        max_ = 0

        def inbound(idx):
            return 0 <= idx < N

        def find(x):
            root = x

            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                x, parent[x] = parent[x], root

            return root

        def union(x, y):
            x_rep = find(x)
            y_rep = find(y)

            if x_rep != y_rep:
                if size[x_rep] >= size[y_rep]:
                    size[x_rep] += size[y_rep]
                    parent[y_rep] = parent[x_rep]
                    sum_[x_rep] += sum_[y_rep]
                else:
                    size[y_rep] += size[x_rep]
                    parent[x_rep] = parent[y_rep]
                    sum_[y_rep] += sum_[x_rep]
        
        for idx in range(N-1, -1, -1):
            ans[idx] = max_
            i = removeQueries[idx]
            
            if inbound(i-1) and check[i-1] != 0:
                union(i, i-1)
            
            if inbound(i+1) and check[i+1] != 0:
                union(i, i+1)
                
            max_ = max(max_, sum_[find(i)], nums[i])
            check[i] = nums[i]
        
        return ans