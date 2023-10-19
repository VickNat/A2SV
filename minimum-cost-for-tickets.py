class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        travelNeeded = defaultdict(bool)

        for day in days:
            travelNeeded[day] = True
        
        @cache
        def dp(curDay):
            if curDay > days[-1]:
                return 0

            if not travelNeeded[curDay]:
                return dp(curDay+1)

            oneDay = costs[0] + dp(curDay+1)
            sevenDays = costs[1] + dp(curDay+7)
            thirtyDays = costs[2] + dp(curDay+30)

            return min(oneDay, sevenDays, thirtyDays)
        
        return dp(1)