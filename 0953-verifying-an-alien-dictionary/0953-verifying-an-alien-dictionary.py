from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = dict()
        # value = 0
        orderList = list(order)
        
        for letter in orderList:
            alphabets[letter] = orderList.index(letter)
            # value+=1
            
        idx1 = 0
        
        for idx1 in range(idx1, len(words)):
            word1 = words[idx1]
            idx2 = idx1+1
            
            for idx2 in range(idx2, len(words)):
                word2 = words[idx2]
                letterIdx = 0
                
                while letterIdx < len(word2):
                    word1Letter = word1[letterIdx]
                    word2Letter = word2[letterIdx]
                    
                    if alphabets[word1Letter] < alphabets[word2Letter] and letterIdx+1 != len(word1):
                        break
                        
                    if alphabets[word1Letter] > alphabets[word2Letter]:
                        return False
                    elif letterIdx+1 == len(word1) and alphabets[word1Letter] == alphabets[word2Letter] and len(word1) <= len(word2):
                        break
                    elif letterIdx+1 == len(word2) and alphabets[word1Letter] ==alphabets[word2Letter] and len(word1) > len(word2):
                        return False
                    else:
                        letterIdx += 1
            
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dictionary = defaultdict(int)
        
#         for idx in range(len(order)):
#             dictionary[order[idx]] = idx
        
#         testWord = words[0]
        
#         for index in range(len(words)):
#             for letter in range(len(testWord)):
#                 if  len(testWord)>len(words[index]):
#                     return False
#                 elif dictionary[testWord[letter]]>dictionary[words[index][letter]]:
#                     return False
            
#             testWord = words[index]
                
#         return True
                    
            