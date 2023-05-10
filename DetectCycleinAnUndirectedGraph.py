from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
	    visited = set()
		
		def bfs(idx):
		    queue = deque([(idx, -1)])
		    
		    while queue:
		        cur, par = queue.popleft()
		        
		        for elm in adj[cur]:
		            if elm not in visited:
		                queue.append((elm, cur))
		                visited.add(elm)
		            elif elm in visited and elm != par:
		                return False
		                
		    return True

		for idx in range(V):
		    if idx not in visited:
		        visited.add(idx)
		        if not bfs(idx):
		            return 1
		return 0
		