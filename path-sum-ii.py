# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        visited = set()
        
        def dfs(node, path, sum_):
            
            visited.add(node)
            ans = []

            if sum_ == targetSum and not node.right and not node.left:
                return [path[:]]
            
            if node.left and node.left not in visited:
                ans += dfs(node.left, path[:]+[node.left.val], sum_+node.left.val)
            if node.right and node.right not in visited:
                ans += dfs(node.right, path[:]+[node.right.val], sum_+node.right.val)
            
            return ans
        
        if root:
            return dfs(root, [root.val], root.val)
        return []