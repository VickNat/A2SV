class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        N = len(s)
        string = s[::-1]
        hashValues = {chr(97+i): i+1 for i in range(26)}
        ans = ""

        compare = 0
        exponent = k-1

        powers = [1]
        for _ in range(N):
            powers.append((powers[-1] * power) % modulo)

        for i in range(k):
            compare += (hashValues[string[i]] * powers[exponent]) % modulo
            exponent -= 1

        if compare % modulo == hashValue:
            temp = string[:k]
            ans = temp[::-1]

        exponent = k-1

        i = k
        j = 0
        while i < N:
            compare -= (hashValues[string[j]] * powers[exponent]) % modulo
            compare *= power % modulo
            compare += hashValues[string[i]] % modulo

            if compare % modulo == hashValue:
                temp = string[j+1:i+1]
                ans = temp[::-1]

            j += 1
            i += 1

        return ans