# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBst(self, root):
        if not root:
            return []
        

        left = self.isBst(root.left)
        right = self.isBst(root.right)
        
        ans = []
        ans.extend(left)
        ans.append(root.val)
        ans.extend(right)

        return ans

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bst = self.isBst(root)
        check = set(sorted(bst))
        check = list(check)
        check.sort()
        return bst == check