# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumCalculator(self, root):
        if not root:
            return [0, 0]
        
        left = self.sumCalculator(root.left)
        right = self.sumCalculator(root.right)

        calculate = [left[0]+right[0]+1, left[1]+right[1]+root.val]
        if calculate[1]//calculate[0] == root.val:
            self.average += 1
        
        return calculate

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.average = 0
        self.sumCalculator(root)

        return self.average