# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):           
            ans = []
            
            if node.left:
                ans += dfs(node.left)
            
            ans += [node.val]

            if node.right:
                ans += dfs(node.right)
            
            return ans
        
        ans = dfs(root)
        comp = sorted(ans)

        if len(set(ans)) != len(ans):
            return False
        return ans[:] == comp[:]