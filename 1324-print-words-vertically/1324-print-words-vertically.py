class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxLength = 0
        listOfS = list(s.split(" "))
        verticalPrint = []
        
#         Max Length is needed to iterate through each word till the maximum word length is reached
        for word in listOfS:
            maxLength = max(maxLength, len(word))
        
        for letterIdx in range(maxLength):
            temp = []
            
#             To add the letters vertically
            for words in range(len(listOfS)):
                if letterIdx >= len(listOfS[words]):
                    temp.append(" ")
                else:
                    temp.append(listOfS[words][letterIdx])
                
            spaceCheck = len(temp)-1
            
#             To remove last elements of space
            while spaceCheck >= 0 and temp[spaceCheck] == " ":
                temp.pop()
                spaceCheck = len(temp)-1
            
            verticalPrint.append("".join(temp))
        
        return verticalPrint