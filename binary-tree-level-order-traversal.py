# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        kCount = defaultdict(list)

        def order(root, h):
            if not root:
                return
            kCount[h].append(root.val)
            left = order(root.left, h+1)
            right = order(root.right, h+1)

        order(root, 0)
        return list(kCount.values())