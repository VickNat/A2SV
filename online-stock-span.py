class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        counts = 1
        while self.stack and self.stack[-1][0] <= price:
            counts += self.stack.pop()[1]
        
        self.stack.append([price, counts])
        return counts 




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)