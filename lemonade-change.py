class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        ans = True

        for bill in bills:
            if bill == 5:
                change[bill] += 1
            elif bill == 10:
                if change[5] >= 1:
                    change[5] -= 1
                    change[10] += 1
                else:
                    ans = False
                    break
            else:
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif not change[10] and change[5] >= 3:
                    change[5] -= 3
                else:
                    ans = False
                    break
                change[20] += 1
        
        return ans