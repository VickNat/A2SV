class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        if len(self.smallHeap) == len(self.largeHeap):
            heappush(self.largeHeap, -heappushpop(self.smallHeap, -num))
        else:
            heappush(self.smallHeap, -heappushpop(self.largeHeap, num))
    
    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            return (self.largeHeap[0] - self.smallHeap[0]) / 2.0
        return self.largeHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()