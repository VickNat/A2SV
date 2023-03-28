class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        N = len(requests)
        valid = 0
        check = [0]*n

        def backtrack(net, ptr, counts):
            nonlocal valid
            if ptr >= N:
                if check == net:
                    valid = max(counts, valid)
                return

            start = requests[ptr][0]
            end = requests[ptr][1]
            temp = net[:]

            net[start] -= 1
            net[end] += 1
            
            backtrack(net[:], ptr+1, counts+1)
            backtrack(temp[:], ptr+1, counts)
        
        net = [0]*n

        backtrack(net, 0, 0)

        return valid