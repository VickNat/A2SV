class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v4 = queryIP.split(".")
        v6 = queryIP.split(":")
        ipv4 = False
        ipv6 = False

        if len(v4) == 4:
            ipv4 = True
            for val in v4:
                if (not val.isdigit()) or (str(int(val)) != val) or (int(val) > 255):
                    ipv4 = False
                    break
        

        if len(v6) == 8:
            ipv6 = True
            for val in v6:
                hexa = True
                hexVals = {"A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"}

                for c in val:
                    if c.isalpha() and c not in hexVals:
                        hexa = False
                        break

                if (len(val) == 0) or (len(val) > 4) or not hexa:
                    ipv6 = False
                    break

        if ipv4:
            return "IPv4"
        if ipv6:
            return "IPv6"
        return "Neither"