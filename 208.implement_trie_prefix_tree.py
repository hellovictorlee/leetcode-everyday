class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = dict()
            trie = trie[c]
        trie['#'] = '#'
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return '#' in trie
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.trie
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
