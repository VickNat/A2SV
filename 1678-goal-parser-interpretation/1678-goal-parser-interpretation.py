class Solution:
    def interpret(self, command: str) -> str:
        goalParser = ""
        length = len(command)
        index = 0
        
        while index<length:
            if command[index] == "G":
                goalParser += "G"
                index += 1
            elif command[index:index+2] == "()":
                goalParser += "o"
                index += 2
            else:
                goalParser += "al"
                index += 4
        
        return goalParser
        