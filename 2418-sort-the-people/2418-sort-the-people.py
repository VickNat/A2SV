class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            minIdx = i
            for j in range(i+1, len(heights)):
                
                if heights[minIdx] < heights[j]:
                    minIdx = j
                    
            names[i], names[minIdx] = names[minIdx], names[i]
            heights[i], heights[minIdx] = heights[minIdx], heights[i]
            
        return names