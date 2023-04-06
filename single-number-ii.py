class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        max_ = max(max(nums), abs(min(nums)))
        val = 1
        ans = 0

        while val <= max_:
            add = 0

            for num in nums:
                temp = 1
                if val&(abs(num)) == 0:
                    temp = 0
                add += temp

            add %= 3
            if add >= 1:
                add = 1

            ans |= add<<(val.bit_length()-1)
            val <<= 1

        if ans not in nums:
            ans = -ans
        elif ans in nums and -ans in nums:
            nums.remove(ans)

            if ans in nums:
                ans = -ans

        return ans