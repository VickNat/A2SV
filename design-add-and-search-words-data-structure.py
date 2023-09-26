class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]

        cur.endOfWord = True

    def searchHelper(self, cur, word):
        for i, c in enumerate(word):
            if c == ".":
                for key, val in cur.children.items():
                    if self.searchHelper(cur.children[key], word[i+1:]):
                        return True
                return False
            else:
                if c in cur.children:
                    cur = cur.children[c]
                else:
                    return False

        return cur.endOfWord
    def search(self, word: str) -> bool:
        cur = self.root
        return self.searchHelper(cur, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)