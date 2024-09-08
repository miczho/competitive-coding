"""
N = number of words
M = max length of words
V = number of nodes/vertices (number of unique chars)
E = number of edges

Time Complexity:
O(N * M + N * M + V + E)
= O(N * M + V + E)
= O(building graph (aka N * M) + traversing graph (aka V + E))

Space Complexity:
O(E + V + V)
= O(V + E)

https://neetcode.io/problems/foreign-dictionary
https://leetcode.com/problems/alien-dictionary

#2024 #blind75 #neetcode150 #topSort
"""

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        children = defaultdict(lambda: set())
        inDegree = {ch: 0 for word in words for ch in word}
        queue = []

        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]

            for j in range(len(word1)):
                if j >= len(word2):
                    return ""

                parent, child = word1[j], word2[j]

                if parent != child:
                    if child not in children[parent]:
                        children[parent].add(child)
                        inDegree[child] += 1
                    break

        for key, value in inDegree.items():
            if value == 0:
                queue.append(key)

        for node in queue:
            for child in children[node]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)

        return "".join(queue) if len(queue) == len(inDegree) else ""
