class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        countPairDomain = []
        pairDomain = defaultdict(int)
        
        for domain in cpdomains:
            visitCount, visitDomain = domain.split(" ")
            
            pairDomain[visitDomain] += int(visitCount)
            
            for word in range(len(visitDomain)):
                if visitDomain[word] == ".":
                    pairDomain[visitDomain[word+1:]] += int(visitCount)
            
        for key in pairDomain:
            temp = str(pairDomain[key]) + " " + key
            countPairDomain.append(temp)
            
        return countPairDomain