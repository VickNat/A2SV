# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nodeCounts = defaultdict(list)
        max_ = -1

        def dfs(node, h):
            if not node:
                return
            if node.left:
                node.left.val = 2 * node.val
            if node.right:
                node.right.val = 2 * node.val + 1
            
            nodeCounts[h].append(node.val)
            dfs(node.left, h+1)
            dfs(node.right, h+1)
        
        root.val = 1
        dfs(root, 0)

        for key, val in nodeCounts.items():
            max_ = max(max_, val[-1]-val[0])
        
        return max_+1