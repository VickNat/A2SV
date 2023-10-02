class TrieNode:
    def __init__(self):
        self.children={}
        self.idx = -1

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str, idx) -> None:
        cur=self.root

        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
                
            cur=cur.children[c]
            cur.idx = idx

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return -1
            cur=cur.children[c]
        return cur.idx     

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for idx, word in enumerate(words):
            for i in range(len(word)):
                self.trie.insert(word[i:]+"{"+word, idx)        

    def f(self, pref: str, suff: str) -> int:
        return self.trie.startsWith(suff+"{"+pref)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)