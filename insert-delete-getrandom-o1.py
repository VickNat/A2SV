class RandomizedSet:

    def __init__(self):
        self.randomizedSet = set()
        self.randomizedList = []
        
    def insert(self, val: int) -> bool:
        if val in self.randomizedSet:
            return False
        
        self.randomizedSet.add(val)
        self.randomizedList.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomizedSet:
            return False

        self.randomizedSet.remove(val)
        self.randomizedList.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.randomizedList)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()