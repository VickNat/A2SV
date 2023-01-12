class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicateHash = defaultdict(list)
        duplicate = []
        
        for path in paths:
            directory = path.split(" ")
            root = directory[0]
            
            for direct in range(1, len(directory)):
                temp = directory[direct]
                start = temp.index("(")
                filePath = root + "/" + temp[:start]
                
                fileName = temp[start+1:len(temp)-1]
                duplicateHash[fileName].append(filePath)
            
        for val in duplicateHash.values():
            if(len(val)>1):
                duplicate.append(val)
        
        return duplicate
                