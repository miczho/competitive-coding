"""
Initially thought of using BFS, but a traversal algo is not needed.
This is bc of the path counter variable.

Code can be cleaned up to look more readable.

Time Complexity:
O(N^2) where N = length of 'board'

Space Complexity:
O(N^2) where N = length of 'board'

https://leetcode.com/problems/number-of-paths-with-max-score

#2024
"""

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(board)
        score = defaultdict(lambda: [0, 0])
        move = ((1, 0), (0, 1), (1, 1))

        def getBoardCell(x, y):
            return int(board[x][y]) if board[x][y].isdigit() else 0

        score[(n - 1, n - 1)] = [0, 1]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] != "X":
                    for iMove, jMove in move:
                        currScore = score[(i + iMove, j + jMove)]
                        if currScore[1] > 0:
                            newScore = currScore[0] + getBoardCell(i, j)

                            if newScore > score[(i, j)][0]:
                                score[(i, j)] = [newScore, currScore[1]]
                            elif newScore == score[(i, j)][0]:
                                score[(i, j)][1] += currScore[1]
                                score[(i, j)][1] %= MOD

        return score[(0, 0)]
