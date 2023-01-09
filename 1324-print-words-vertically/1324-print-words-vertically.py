class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxLength = 0
        listOfS = list(s.split(" "))
        answer = []
        
        for word in listOfS:
            maxLength = max(maxLength, len(word))
        
        for letterIdx in range(maxLength):
            temp = []
            
            for words in range(len(listOfS)):
                if letterIdx >= len(listOfS[words]):
                    temp.append(" ")
                elif letterIdx < len(listOfS[words]):
                    temp.append(listOfS[words][letterIdx])
                
            spaceCheck = len(temp)-1
            
            while spaceCheck >= 0 and temp[spaceCheck] == " ":
                temp.pop()
                spaceCheck = len(temp)-1
            
            answer.append("".join(temp))
        
        return answer