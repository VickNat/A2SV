# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(root):
            if not root:
                return
            if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
                return root
            if p.val == root.val:
                return p
            if q.val == root.val:
                return q
            
            if p.val > root.val and q.val > root.val:
                return check(root.right)
            if p.val < root.val and q.val < root.val:
                return check(root.left)

        return check(root)