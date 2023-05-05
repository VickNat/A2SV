class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCounts = defaultdict(int)
        heap = []
        ans = []
        size = 0

        for elm in words:
            wordCounts[elm] += 1
        
        for key, val in wordCounts.items():
            heap.append((-val, key))
        heapify(heap)

        while len(ans) < k:
            ans.append(heappop(heap)[1])

        return ans