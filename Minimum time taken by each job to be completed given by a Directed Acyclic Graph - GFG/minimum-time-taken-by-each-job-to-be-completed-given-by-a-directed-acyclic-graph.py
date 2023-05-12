from typing import List
from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        indegree = defaultdict(int)
        outdegree = defaultdict(list)
        queue = deque()
        levels = 1
        time = [0 for i in range(n)]
        
        for a, b in edges:
            indegree[b] += 1
            outdegree[a].append(b)
        
        for idx in range(1, n+1):
            if not indegree[idx]:
                queue.append(idx)
                time[idx-1] = str(1)

        while queue:
            N = len(queue)
            
            for _ in range(N):
                cur = queue.popleft()
                
                for elm in outdegree[cur]:
                    indegree[elm] -= 1
                    
                    if indegree[elm] == 0:
                        queue.append(elm)
                        time[elm-1] = str(levels+1)
            
            levels += 1
        
        return " ".join(time)
            
            

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends