class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        
        first = salary[0]
        last = salary[-1]
        
        salary.remove(last)
        salary.remove(first)
        
        total = 0
        length = len(salary)
        
        for index in range(len(salary)):
            total += salary[index]
            
        average = total/length
        
        return average