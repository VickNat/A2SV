# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)

        def dp(node):
            if not node:
                return 0
            
            if node in memo:
                return memo[node]
            
            notTake = 0
            notTake += dp(node.left) + dp(node.right)
            take = 0

            if node.left:
                take += dp(node.left.left) + dp(node.left.right)
            if node.right:
                take += dp(node.right.left) + dp(node.right.right)
            
            memo[node] = max(notTake, take+node.val)
            return memo[node]

        dp(root)
        return max(memo.values())