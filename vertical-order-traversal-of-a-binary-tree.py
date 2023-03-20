# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical = defaultdict(list)
        
        def order(root, r, c):
            if not root:
                return
            coords = [r, root.val]
            vertical[c].append(coords)
            order(root.left, r+1, c-1)
            order(root.right, r+1, c+1)

        order(root, 0, 0)

        Keys = list(vertical.keys())
        Keys.sort()
        ans = {key: vertical[key] for key in Keys}

        fin = []
        for val in ans:
            temp = sorted(ans[val])
            t = []
            for elm in temp:
                t.append(elm[1])
            
            fin.append(t)

        return fin