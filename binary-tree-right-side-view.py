# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSide(self, root, depth):
        if not root:
            return
        
        self.rightDict[depth] = root.val
        left = self.rightSide(root.left, depth+1)
        right = self.rightSide(root.right, depth+1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.rightDict = defaultdict(int)
        self.rightSide(root, 1)

        return list(self.rightDict.values())