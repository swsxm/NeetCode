class Node:
    def __init__(self):
        self.values = {}
        self.endOfW = False


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.values:
                curr.values[i] = Node()
            curr = curr.values[i]
        curr.endOfW = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i in curr.values:
                curr = curr.values[i]
            else:
                return False
        return curr.endOfW

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i not in curr.values:
                return False
            curr = curr.values[i]
        return True
