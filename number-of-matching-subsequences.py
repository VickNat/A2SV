class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.wordCounts = 0
        
class Solution:
    def __init__(self):
        self.root=TrieNode()
        self.matchCounts = 0

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
                
            cur=cur.children[c]
        cur.endOfWord=True
        cur.wordCounts += 1
    
    def indexFinder(self, word, start, char):
        for i in range(start, len(word)):
            c = word[i]
            if c == char:
                return i
        return -1

    def dfs(self, word, node, idx):
        for i in range(26):
            c = chr(i+ord("a"))

            if c in node.children:
                child = node.children[c]
                wordIdx = self.indexFinder(word, idx, c)
                if wordIdx != -1:
                    if child.endOfWord:
                        self.matchCounts += child.wordCounts
                    self.dfs(word, child, wordIdx+1)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        for word in words:
            self.insert(word)

        self.dfs(s, self.root, 0)
        
        return self.matchCounts