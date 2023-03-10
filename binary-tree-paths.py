# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        ans = []
        ans.extend(left)
        ans.extend(right)

        for idx in range(len(ans)):
            ans[idx] = str(root.val) + "->" + ans[idx]
        
        return ans