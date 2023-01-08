class Solution:
    def interpret(self, command: str) -> str:
        result = []
        letter = 0
        
        while letter < len(command):
            if command[letter] == "G":
                result.append("G")
                letter += 1
            elif command[letter] == "(" and command[letter+1] == ")":
                result.append("o")
                letter += 2
            else:
                result.append("al")
                letter+=4
        
        return "".join(result)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         goalParser = ""
#         length = len(command)
#         index = 0
        
#         while index<length:
#             if command[index] == "G":
#                 goalParser += "G"
#                 index += 1
#             elif command[index:index+2] == "()":
#                 goalParser += "o"
#                 index += 2
#             else:
#                 goalParser += "al"
#                 index += 4
        
#         return goalParser
        