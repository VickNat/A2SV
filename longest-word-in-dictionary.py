class TrieNode:
    def __init__(self):
        self.children=[None for i in range(26)]
        self.endOfWord=False

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        cur=self.root

        for c in word:
            asci = ord(c)-ord("a")
            
            if cur.children[asci] == None:
                cur.children[asci]=TrieNode()
                
            cur=cur.children[asci]
        cur.endOfWord=True    

    def startsWith(self, prefix):
        cur=self.root

        for c in prefix:
            asci = ord(c)-ord("a")

            if cur.children[asci].endOfWord == False:
                return False
            
            cur = cur.children[asci]
        
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        ans = ""

        for word in words:
            if trie.startsWith(word):
                if len(ans) < len(word):
                    ans = word
                elif len(ans) == len(word) and word < ans:
                    ans = word
        
        return ans