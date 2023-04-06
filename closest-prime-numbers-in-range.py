class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True]*(right+1)
        primes[0] = primes[1] = False
        rangedPrime = []
        ans = [-1,-1]
        min_ = float('inf')

        for idx in range(right+1):
            if primes[idx] == False:
                continue

            multiple = idx+idx

            while multiple <= right:
                primes[multiple] = False
                multiple += idx
            
            if idx >= left:
                rangedPrime.append(idx)

        for i in range(len(rangedPrime)-1):
            val = rangedPrime[i+1] - rangedPrime[i]
            if val < min_:
                ans[0] = rangedPrime[i]
                ans[1] = rangedPrime[i+1]
                min_ = val
        
        return ans