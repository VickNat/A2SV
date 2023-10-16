# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        duplicates = defaultdict()
        ans = set()

        def dfs(node):
            nonlocal ans
            if not node:
                return "N" 

            curSerial = str(node.val)
            curSerial += "," + dfs(node.left)
            curSerial += "," + dfs(node.right)

            if curSerial in duplicates:
                ans.add(duplicates[curSerial])
            else:
                duplicates[curSerial] = node
            
            return curSerial

        dfs(root)
        return list(ans)