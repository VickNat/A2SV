class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        folder = ''
        
        for elm in path + '/':
            if elm == '/':
                if folder == '..':
                    if stack: stack.pop()
                elif folder != '' and folder != '.':
                    stack.append(folder)
                
                folder = ''
            else:
                folder += elm
            
        return '/' + '/'.join(stack)