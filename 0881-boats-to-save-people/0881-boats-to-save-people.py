class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        left = 0
        right = len(people)-1
        
        people.sort()
        
        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
            elif people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                boats += 1
                break
            
            boats += 1
        
        return boats