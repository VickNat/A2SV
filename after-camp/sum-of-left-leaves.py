# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(cur, isLeft):
            nonlocal ans
            if not cur:
                return
            if isLeft and not cur.left and not cur.right:
                ans += cur.val
            
            dfs(cur.right, False)
            dfs(cur.left, True)

        dfs(root, False)
        return ans