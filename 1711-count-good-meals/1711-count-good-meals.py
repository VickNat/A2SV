class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = []
        numDict = defaultdict(int)
        goodMeals = 0
        
        for idx in range(22):
            powers.append(2**idx)
                        
        for index in range(len(deliciousness)):
            for power in powers:
                diff = power - deliciousness[index]
                if diff in numDict:
                    goodMeals += numDict[diff]
                    
            numDict[deliciousness[index]] += 1
        
        return goodMeals % (10**9 + 7)
                