"""
#dfs #backtracking
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def isValid(x, y, val):
            for i in range(9):
                if board[i][y] == val or board[x][i] == val:
                    return False
                if board[3 * (x // 3) + i // 3][3 * (y // 3) + i % 3] == val:
                    return False

            return True

        # DFS
        def solve(x, y):
            if x == 9 and y == 0: 
                return True
            if board[x][y] != '.': 
                return solve(x+1 if y == 8 else x, 0 if y == 8 else y+1)

            for i in range(ord('1'), ord(':')):
                if isValid(x, y, chr(i)):
                    # Setting a possible value
                    board[x][y] = chr(i);
                    
                    # Recurively checking if we can solve the board
                    if solve(x+1 if y == 8 else x, 0 if y == 8 else y+1):
                        return True

                    # Backtracking if we find out that this value does not work
                    board[x][y] = '.'

            return False

        solve(0, 0)