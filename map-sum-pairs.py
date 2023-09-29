class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
        self.sum_ = 0

class MapSum:

    def __init__(self):
        self.mapSums = defaultdict(int)
        self.root=TrieNode()        

    def insert(self, key: str, val: int) -> None:
        add = 0
        if key in self.mapSums:
            add = self.mapSums[key]-val
        self.mapSums[key] = val
        cur = self.root

        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            if add != 0:
                cur.children[c].sum_ -= add
            else:
                cur.children[c].sum_ += val

            cur = cur.children[c]

        cur.endOfWord = True

    def sum(self, prefix: str) -> int:
        cur=self.root

        for c in prefix:
            if c not in cur.children:
                return 0
            cur=cur.children[c]
        return cur.sum_   


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)