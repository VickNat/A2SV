class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        duplicates = defaultdict(int)
        size = len(s)
        stack = []
        letters = set()
        
        for elm in s:
            duplicates[elm] += 1
        
        for elm in s:
            while stack and stack[-1] >= elm and duplicates[stack[-1]] > 0:
                if elm not in letters or stack[-1] == elm:
                    letters.remove(stack[-1])
                    stack.pop()
                else:
                    break
                    
            if elm not in letters:
                stack.append(elm)
                letters.add(elm)
                
            duplicates[elm] -= 1
        
        return "".join(stack)