# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = defaultdict(int)

        def finder(root):
            if not root:
                return

            modes[root.val] += 1
            left = finder(root.left)
            right = finder(root.right)

        finder(root)
        maxVal = max(modes.values())
        ans = []
        
        for elm in modes:
            if modes[elm] == maxVal:
                ans.append(elm)

        return ans