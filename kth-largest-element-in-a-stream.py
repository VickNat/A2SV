class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        self.kCounts = 0

        for num in nums:
            heappush(self.heap, num)
            self.kCounts += 1

            if self.kCounts > self.k:
                heappop(self.heap)
                self.kCounts -= 1

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        self.kCounts += 1

        if self.kCounts > self.k:
            heappop(self.heap)
            self.kCounts -= 1

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)