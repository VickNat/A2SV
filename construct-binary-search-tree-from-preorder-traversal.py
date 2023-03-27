# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def bst(root, val):
            temp = TreeNode(val)

            if not root:
                return temp
            
            if root.val > val:
                root.left = bst(root.left, val)
            elif root.val < val:
                root.right = bst(root.right, val)
            
            return root
        
        root = None
        for elm in preorder:
            root = bst(root, elm)
        
        return root