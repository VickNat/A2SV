class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.ans = []
        self.counts = 0
        
    def consec(self, num: int) -> bool:
        self.ans.append(num)

        if num == self.value:
            self.counts += 1
        else:
            self.counts = 0
        
        if self.counts > self.k:
            self.counts -= 1

        if self.k > len(self.ans):
            return False
            
        if self.counts == self.k:
            return True
        
        return False

        
        
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)