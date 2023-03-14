# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(rootL, rootR):
            if not rootL and not rootR:
                return True
            if not rootL or not rootR:
                return False
            
            left = check(rootL.left, rootR.right)
            right = check(rootL.right, rootR.left)

            if left and right:
                if rootL.val == rootR.val:
                    return True
            
            return False
        
        return check(root.left, root.right)