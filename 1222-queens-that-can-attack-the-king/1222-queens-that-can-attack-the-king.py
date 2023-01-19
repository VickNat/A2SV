class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attacks = []
        xKing = king[0]
        yKing = king[1]
        tempKing = [xKing, yKing]
        rows = 8
        cols = 8
        
#         Up check
        while xKing >= 0:
            tempKing = [xKing, yKing]
            
            if tempKing in queens:
                attacks.append(tempKing)
                break
            else:
                xKing -= 1
        
        xKing = king[0]
        tempKing = [xKing, yKing]
        
#         Down check
        while xKing < rows:
            tempKing = [xKing, yKing]
            
            if tempKing in queens:
                attacks.append(tempKing)
                break
            else:
                xKing += 1
        
        xKing = king[0]
        tempKing = [xKing, yKing]
        
#         Left check
        while yKing >= 0:
            tempKing = [xKing, yKing]
            
            if tempKing in queens:
                attacks.append(tempKing)
                break
            else:
                yKing -= 1
            
        yKing = king[1]
        tempKing = [xKing, yKing]
        
#         Right check
        while yKing < cols:
            tempKing = [xKing, yKing]
            
            if tempKing in queens:
                attacks.append(tempKing)
                break
            else:
                yKing += 1
            
        yKing = king[1]
        tempKing = [xKing, yKing]
        
#         Diagonal up right check
        while xKing >= 0 and yKing < cols:
            tempKing = [xKing, yKing]
            
            if tempKing in queens:
                attacks.append(tempKing)
                break
            else:
                xKing -= 1
                yKing += 1
        
        xKing = king[0]
        yKing = king[1]
        tempKing = [xKing, yKing]
        
#         Diagonal right down check
        while xKing < rows and yKing < cols:
            tempKing = [xKing, yKing]
            
            if tempKing in queens:
                attacks.append(tempKing)
                break
            else:
                xKing += 1
                yKing += 1
        
        xKing = king[0]
        yKing = king[1]
        tempKing = [xKing, yKing]
        
#         Diagonal left up check
        while xKing >= 0 and yKing >= 0:
            tempKing = [xKing, yKing]
            
            if tempKing in queens:
                attacks.append(tempKing)
                break
            else:
                xKing -= 1
                yKing -= 1
        
        xKing = king[0]
        yKing = king[1]
        tempKing = [xKing, yKing]
        
#         Diagonal left down check
        while xKing < rows and yKing >= 0:
            tempKing = [xKing, yKing]
            
            if tempKing in queens:
                attacks.append(tempKing)
                break
            else:
                xKing += 1
                yKing -= 1
        
        return attacks