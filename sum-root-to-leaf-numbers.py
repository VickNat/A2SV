# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        sum_ = 0

        def dfs(node, num):
            if not node:
                return
            if not node.left and not node.right:
                num += str(node.val)
                ans.append(num)
                return
            
            num += str(node.val)
            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, "")

        for num in ans:
            sum_ += int(num)

        return sum_