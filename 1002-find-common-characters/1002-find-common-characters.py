class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = defaultdict(int)
        common = []
        
        for check in words[0]:
            letters[check] += 1
        
        for letter in letters:
            for word in range(1, len(words)):
                if letters[letter] == 1 and letter not in words[word]:
                    letters[letter] -= 1
                elif letters[letter] > 1:
                    counts = 0
                    
                    for idx in words[word]:
                        if idx == letter:
                            counts += 1
                    
                    letters[letter] = min(letters[letter], counts)
                
        for key in letters:
            if letters[key] >= 1:
                for index in range(letters[key]):
                    common.append(key)
        
        return common