class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.maxVoted = self.persons[0]
        self.topCand = []
        self.votes = defaultdict(int)
        self.size = len(self.persons)

        for idx in range(self.size):
            self.votes[self.persons[idx]] += 1
            if self.votes[self.persons[idx]] >= self.votes[self.maxVoted]:
                self.maxVoted = self.persons[idx]
            
            self.topCand.append(self.maxVoted)

    def q(self, t: int) -> int:        
        left = -1
        right = self.size

        while left+1 < right:
            mid = left + (right-left)//2

            if self.times[mid] <= t:
                left = mid
            else:
                right = mid

        return self.topCand[left]
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)