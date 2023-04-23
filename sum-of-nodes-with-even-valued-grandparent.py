# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_ = 0

        def dfs(parent, gParent, node):
            nonlocal sum_

            if not node:
                return

            if gParent > 0 and gParent%2 == 0:
                sum_ += node.val

            dfs(node.val, parent, node.left)
            dfs(node.val, parent, node.right)
        
        dfs(0, 0, root)
        return sum_