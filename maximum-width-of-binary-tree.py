# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        kCount = defaultdict(list)
        maxWidth = -1
        root.val == 1
        
        def order(root, h):
            nonlocal maxWidth
            if not root:
                return
            if root.left:
                root.left.val = 2*root.val
            if root.right:
                root.right.val = (2*root.val)+1

            kCount[h].append(root.val)
            order(root.left, h+1)
            order(root.right, h+1)

        order(root, 0)

        for value in kCount.values():
            maxWidth = max(maxWidth, value[-1]-value[0]+1)
            
        return maxWidth