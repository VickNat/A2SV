class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
        self.prefSum = 0

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()

            cur.children[c].prefSum += 1
            cur=cur.children[c]
        cur.endOfWord=True    

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        ans = 0
        for c in prefix:
            ans += cur.children[c].prefSum
            cur=cur.children[c]
            
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        ans = []

        for word in words:
            trie.insert(word)
        
        for word in words:
            ans.append(trie.startsWith(word))
        
        return ans