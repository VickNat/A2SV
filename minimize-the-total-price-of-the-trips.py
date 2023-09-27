class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        freq = [0]*n
        graph = [[] for i in range(n)]
        memo = defaultdict(int)

        # Build graph
        for first, sec in edges:
            graph[first].append(sec)
            graph[sec].append(first)

        # Count frequencies using dfs
        def dfs(cur, end, prev):
            if cur == end:
                freq[cur] += 1
                return True
            
            isPath = False
            
            for child in graph[cur]:
                if child != prev:
                    isPath = isPath or dfs(child, end, cur)
            
            if isPath:
                freq[cur] += 1
            return isPath
            
        for start, end in trips:
            dfs(start, end, -1)

        # Build a top down dp to find min path sum
        def dp(cur, prev, halfIt):
            ans = price[cur]*freq[cur]

            if halfIt:
                ans //= 2

            if (cur, halfIt) in memo:
                return memo[(cur, halfIt)]
            
            if halfIt:
                for child in graph[cur]:
                    if child != prev:
                        ans += dp(child, cur, False)
            else:
                for child in graph[cur]:
                    if child != prev:
                        ans += min(dp(child, cur, False), dp(child, cur, True))
            
            memo[(cur, halfIt)] = ans
            return ans
        
        return min(dp(0, -1, False), dp(0, -1, True))