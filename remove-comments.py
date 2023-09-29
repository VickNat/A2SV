class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []        
        is_comment = ""
        substring = ""        
        for line in source:
            i = 0
            while i < len(line):
                if not is_comment and line[i:i+2] == '//':
                    break

                elif line[i:i+2] == '/*':
                    if not is_comment:
                        is_comment = True
                        i += 1

                elif is_comment and line[i:i+2] == '*/':
                    is_comment = False
                    i += 1
                
                elif not is_comment:
                    substring += line[i]                
                    
                i += 1
                
            if substring and not is_comment:
                result.append(substring)
                substring = ""

        return result