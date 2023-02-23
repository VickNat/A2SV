class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)
        maxFruits = 0
        start = 0
        end = 0
        
        for end in range(len(fruits)):
            baskets[fruits[end]] += 1
            
            while len(baskets) > 2:
                baskets[fruits[start]] -= 1
                
                if baskets[fruits[start]] == 0:
                    baskets.pop(fruits[start])

                start += 1
            
            # if len(baskets) == 2:
            maxFruits = max(maxFruits, end - start + 1)
        
        return maxFruits
            
            