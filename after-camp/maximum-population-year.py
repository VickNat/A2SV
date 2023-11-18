class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0 for i in range(101)]

        for birth, death in logs:
            newB = birth - 1950
            newD = death - 1950

            population[newB] += 1
            population[newD] -= 1
        
        for i in range(1, 101):
            population[i] += population[i-1]
        
        max_ = max(population)
        for i in range(101):
            if population[i] == max_:
                return 1950+i