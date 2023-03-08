# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pathSum = -float('inf')

    def pathFinder(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            self.pathSum = max(self.pathSum, root.val)
            return root.val

        left = self.pathFinder(root.left)
        right = self.pathFinder(root.right)

        self.pathSum = max(self.pathSum, left+root.val, right+root.val)

        temp = left + right + root.val
        self.pathSum = max(self.pathSum, temp)

        return max(left+root.val, right+root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathFinder(root)
        return self.pathSum