"""
https://neetcode.io/problems/search-for-word-ii
https://leetcode.com/problems/word-search-ii

#2024 #blind75 #neetcode150
"""

class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, words):
        for word in words:
            node = self.root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]

            node.isWord = True
            node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        With L = average length of word in 'words',
        W = length of 'words'

        Time complexity:
        O(trie construction + DFS search)
        O(W * L + m * n * 4^L)

        Space complexity:
        O(trie + visited arr + DFS call stack)
        O(W * L * 26 + m * n + L)
        """
        m, n = len(board), len(board[0])
        trie = Trie()
        visited = [[False] * n for _ in range(m)]
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        result = set()

        trie.insert(words)

        def dfs(x, y, node):
            visited[x][y] = True

            if node.isWord:
                result.add(node.word)

            for xMove, yMove in moves:
                xNew, yNew = x + xMove, y + yMove

                if 0 <= xNew < m and 0 <= yNew < n:
                    isVisited = visited[xNew][yNew]
                    ch = board[xNew][yNew]

                    if not isVisited and ch in node.children:
                        dfs(xNew, yNew, node.children[ch])

            visited[x][y] = False

        for i in range(m):
            for j in range(n):
                ch = board[i][j]

                if ch in trie.root.children:
                    dfs(i, j, trie.root.children[ch])

        return list(result)
