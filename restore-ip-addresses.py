class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        validIp = []

        def isValid(curr):
            if len(curr) > 1 and curr[0] == '0':
                return False
            if curr and int(curr) > 255:
                return False
            return True

        def backtrack(curr, ptr, ip):
            if len(ip) == 4 and ptr >= N:
                ans = ".".join(ip)
                validIp.append(ans)
                return
            
            for idx in range(ptr, N):
                temp = s[ptr:idx+1]

                if len(ip) == 3:
                    temp = s[ptr:]

                if isValid(temp):
                    ip.append(temp)
                    backtrack(temp, idx+1, ip[:])
                    ip.pop()
                else:
                    return

        backtrack("", 0, [])
        return validIp