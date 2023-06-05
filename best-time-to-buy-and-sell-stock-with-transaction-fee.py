class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        buy = [0]*size
        sell = [0]*size
        buy[0] = -prices[0]

        for idx in range(1, size):
            buy[idx] = max(buy[idx-1], sell[idx-1]-prices[idx])
            sell[idx] = max(sell[idx-1], buy[idx-1]+prices[idx]-fee)
        
        return sell[-1]