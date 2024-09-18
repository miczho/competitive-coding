"""
https://leetcode.com/problems/design-add-and-search-words-data-structure
https://neetcode.io/problems/design-word-search-data-structure

#2024 #blind75 #neetcode150
"""

class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]

        node.isWord = True

    def search(self, word: str) -> bool:
        nodes = [self.root]
        result = False

        for ch in word:
            newNodes = []

            for node in nodes:
                if ch in node.children:
                    newNodes.append(node.children[ch])
                elif ch == ".":
                    for newNode in node.children.values():
                        newNodes.append(newNode)

            nodes = newNodes

        for node in nodes:
            result |= node.isWord

        return result




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)