from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = dict()
        # value = 0
        # orderList = list(order)
        
#         We add the order to alphabets in increasing order
        for letter in order:
            alphabets[letter] = order.index(letter)
            # value+=1
            
        # idx1 = 0
        
        for idx1 in range(len(words)):
            word1 = words[idx1]
            idx2 = idx1+1
            
            for idx2 in range(idx2, len(words)):
                word2 = words[idx2]
                letterIdx = 0
                
#                 While loop to compare the letters in the two words
                while letterIdx < len(word2):
                    word1Letter = word1[letterIdx]
                    word2Letter = word2[letterIdx]
                    
                    if alphabets[word1Letter] < alphabets[word2Letter] and letterIdx+1 != len(word1):
                        break
#                         We break the statement because we need to compare the rest of the words. If i return true here it will not compare the rest of the words in the list
                        
                    if (alphabets[word1Letter] > alphabets[word2Letter]) or (letterIdx+1 == len(word2) and alphabets[word1Letter] == alphabets[word2Letter] and len(word1) > len(word2)):
                        return False
                    elif letterIdx+1 == len(word1) and alphabets[word1Letter] == alphabets[word2Letter] and len(word1) <= len(word2):
                        break
#                         similar reason as the first break statement

                    # elif letterIdx+1 == len(word2) and alphabets[word1Letter] == alphabets[word2Letter] and len(word1) > len(word2):
                    #     return False
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
                    
            