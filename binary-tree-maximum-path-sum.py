# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pathSum = -float('inf')

    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        leftPath = root.val + left
        rightPath = root.val + right
        path = left + right + root.val

        self.pathSum = max(self.pathSum, leftPath, rightPath, path, root.val)
        return max(leftPath, rightPath, root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.pathSum