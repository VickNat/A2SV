# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, root):
        if not root:
            return root

        root.left, root.right = root.right, root.left

        left = self.invert(root.left)
        right = self.invert(root.right)

        return root

    def check(self, root1, root2):
        if not root1 and not root2:
            return True
        elif (root1 and not root2) or (root2 and not root1):
            return False
        
        left = self.check(root1.left, root2.left)
        right = self.check(root1.right, root2.right)

        if left and right and root1.val == root2.val:
            return True
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        inverted = self.invert(root.right)
        ans = self.check(root.left, inverted)
        
        return ans