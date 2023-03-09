# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 and root2 or root1 and not root2:
            return False
        
        left = self.check(root1.left, root2.left)
        right = self.check(root1.right, root2.right)

        if left and right and root1.val == root2.val:
            return True
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p, q)