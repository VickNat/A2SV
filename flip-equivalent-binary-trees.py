# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if not node1:
                if node2:
                    return False
                return True
            
            if node1 and not node2:
                return False
            
            ans = False
            
            if node1.val != node2.val:
                return False

            left = False
            left = left or dfs(node1.left, node2.left)
            left = left or dfs(node1.left, node2.right)

            right = False
            right = right or dfs(node1.right, node2.left)
            right = right or dfs(node1.right, node2.right)

            return ans or (left and right)
        
        return dfs(root1, root2)