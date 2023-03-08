# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sums = 0
        self.counts = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sumGrandChildren(root):
            self.counts += 1
            if not root:
                self.counts -= 1
                return

            if self.counts == 3:
                self.sums += root.val
                self.counts -= 1
                return

            left = sumGrandChildren(root.left)
            right = sumGrandChildren(root.right)
            self.counts -= 1
            return

        if not root:
            return
        
        if root.val%2 == 0:
            sumGrandChildren(root)
        
        left = self.sumEvenGrandparent(root.left)
        right = self.sumEvenGrandparent(root.right)

        return self.sums