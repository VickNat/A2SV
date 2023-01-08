class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sDict = defaultdict()
        tDict = defaultdict()
        
        for lets in s:
            if lets in sDict.keys():
                sDict[lets]+=1
            else:
                sDict[lets]=1
        
        for lett in t:
            if lett in tDict.keys():
                tDict[lett]+=1
            else:
                tDict[lett]=1
        
        for key in tDict:
            if key not in sDict.keys() or tDict[key]>sDict[key]:
                return key
        