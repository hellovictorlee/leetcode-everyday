class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = dict()
            trie = trie[c]
        trie['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def DFS(i, word, trie):
            if i == len(word):
                return '#' in trie
            # c == '.'
            # c in trie
            c = word[i]
            res = False
            if c == '.':
                for cc in trie.keys():
                    if cc != '#':
                        res = res or DFS(i + 1, word, trie[cc])
            elif word[i] in trie:
                res = res or DFS(i + 1, word, trie[c])
            return res

        return DFS(0, word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
