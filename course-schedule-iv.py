class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[float("inf") for j in range(numCourses)] for _ in range(numCourses)]
        ans = []

        for i, j in prerequisites:
            dp[i][j] = 1
        
        for i in range(numCourses):
            dp[i][i] = 0
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    newCourse = dp[i][k]+dp[k][j]
                    if newCourse < dp[i][j]:
                        dp[i][j] = newCourse
        
        for i, j in queries:
            ans.append(dp[i][j] != float('inf'))
        
        return ans