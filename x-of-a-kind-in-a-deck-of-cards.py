class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = defaultdict(int)

        for val in deck:
            counts[val] += 1
        
        ans = [val for val in counts.values()]
        gcd = reduce(math.gcd, ans)

        return gcd>1