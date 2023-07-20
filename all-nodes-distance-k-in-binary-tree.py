# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        children = defaultdict(list)

        def dfs(node, parent):
            if not node:
                return

            dfs(node.left, node.val)
            dfs(node.right, node.val)

            if parent != None:
                children[node.val] = [parent]
            if node.left:
                children[node.val].append(node.left.val)
            if node.right:
                children[node.val].append(node.right.val)
        
        dfs(root, None)

        queue = deque([target.val])
        visited = set()
        visited.add(target.val)
        levels = 0

        while queue:
            N = len(queue)

            for _ in range(N):
                if levels == k:
                    return list(queue)

                node = queue.popleft()
                
                for elm in children[node]:
                    if elm not in visited:
                        visited.add(elm)
                        queue.append(elm)
            
            levels += 1
        return []