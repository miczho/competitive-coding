"""
Given a contiguous block in a board, determine the amount of obstacles you need to destroy for the block to drop to the bottom via gravity.

#interview #incomplete
"""

def dropBlock(board):
    n, m = len(board), len(board[0])
    move = 1
    result = 0

    for i in reversed(range(n)):
        if "*" in board[i]:
            break
        move += 1

    for i in range(n):
        for j in range(m):
            if board[i][j] != "*":
                continue

            for ii in range(i, i + move):
                if board[ii][j] == "#":
                    board[ii][j] == "."
                    result += 1

    return result


if __name__ == "__main__":
    board = [
        ["#", "#", "#", "#", "#"],
        ["#", "*", "*", "*", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        [".", ".", ".", ".", "."]
    ]
    print(dropBlock(board))

    board = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", "*", "*", ".", "."],
        [".", "*", "*", ".", "."],
        [".", ".", ".", ".", "."]
    ]
    print(dropBlock(board))

    board = [
        ["#", "#"],
        ["*", "#"]
    ]
    print(dropBlock(board))

    board = [
        [".", "*", "."],
        ["*", "*", "*"],
        ["*", "#", "*"],
        ["*", "*", "#"],
        [".", ".", "#"]
    ]
    print(dropBlock(board))
