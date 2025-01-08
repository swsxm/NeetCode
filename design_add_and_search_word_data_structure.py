class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.childs:
                cur.childs[c] = TrieNode()
            cur = cur.childs[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, word, i):
            if i == len(word):
                return node.isEnd

            if word[i] == ".":
                for child in node.childs.values():
                    if dfs(child, word, i + 1):
                        return True
                return False
            else:
                if word[i] not in node.childs:
                    return False
                return dfs(node.childs[word[i]], word, i + 1)

        return dfs(self.root, word, 0)
