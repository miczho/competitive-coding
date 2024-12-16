"""
Can also be solved with 2 pointers

https://leetcode.com/problems/expressive-words/

#2024 #revisit
"""


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Solution:
    def expressiveWords(self, s: str, words: list) -> int:
        """
        Trie-esque solution

        Time complexity:
        O(N^2)  (???)
        """

        root = Node()

        for word in words:
            currNode = None
            prevCh = ""
            chCnt = 1

            for ch in word:
                if ch == prevCh:
                    chCnt += 1
                else:
                    currNode = (
                        root
                        if currNode is None
                        else currNode.children.setdefault(f"{prevCh}:{chCnt}", Node())
                    )

                    prevCh = ch
                    chCnt = 1
            currNode = currNode.children.setdefault(f"{prevCh}:{chCnt}", Node())

            currNode.isWord = True

        chFreqs = []
        prevCh = ""
        chCnt = 1
        for ch in s:
            if ch == prevCh:
                chCnt += 1
            else:
                if prevCh != "":
                    chFreqs.append([prevCh, chCnt])
                prevCh = ch
                chCnt = 1
        chFreqs.append([prevCh, chCnt])

        queue = [root]
        for ch, chCnt in chFreqs:
            nextQueue = []

            for node in queue:
                if chCnt < 3:
                    if f"{ch}:{chCnt}" in node.children:
                        nextQueue.append(node.children[f"{ch}:{chCnt}"])
                else:
                    for cnt in range(chCnt):
                        if f"{ch}:{cnt + 1}" in node.children:
                            nextQueue.append(node.children[f"{ch}:{cnt + 1}"])

            queue = nextQueue

        return sum(1 for node in queue if node.isWord)
