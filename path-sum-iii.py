# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counts = 0

        
        def traverse(root, prefixSum):
            nonlocal counts
            if not root:
                return
            
            ptr = len(prefixSum)-1

            for j in range(len(prefixSum)-2, -1, -1):
                val = prefixSum[ptr] - prefixSum[j] + root.val

                if val == targetSum:
                    counts += 1
            
            if root.val == targetSum:
                counts += 1

            prefixSum.append(prefixSum[-1]+root.val)
            traverse(root.left, prefixSum)
            traverse(root.right, prefixSum)
            prefixSum.pop()

        traverse(root, [0])
        return counts