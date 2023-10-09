# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counts = 0

        def dfs(node, prefixSum):
            nonlocal counts
            if not node:
                return
                        
            last = len(prefixSum)-1

            for i in range(len(prefixSum)-2, -1, -1):
                val = prefixSum[last]-prefixSum[i]+node.val

                if val == targetSum:
                    counts += 1
            
            if node.val == targetSum:
                counts += 1

            dfs(node.left, prefixSum[:]+[prefixSum[-1]+node.val])
            dfs(node.right, prefixSum[:]+[prefixSum[-1]+node.val])
        
        dfs(root, [0])
        return counts