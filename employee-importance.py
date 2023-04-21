"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        sum_ = 0
        
        def dfs(importance, subordinate):
            nonlocal sum_

            sum_ += importance

            for elm in subordinate:
                for emp in employees:
                    if emp.id == elm:
                        dfs(emp.importance, emp.subordinates)

        for elm in employees:
            if elm.id == id:
                dfs(elm.importance, elm.subordinates)

        return sum_