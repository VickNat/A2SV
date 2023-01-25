class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right = len(skill)-1
        chemistry = 0
        skillSum = 0
        
        skill.sort()
        
        skillSum = skill[left] + skill[right]
        chemistry += (skill[left] * skill[right])
        left += 1
        right -= 1
        
        while left < right:
            if skill[left] + skill[right] == skillSum:
                chemistry += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                chemistry = -1
                break
        
        return chemistry