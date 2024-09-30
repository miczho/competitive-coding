"""
Given a shape on a board, determine the minimum amount of obstacles you need to destroy for the shape to fall vertically to the bottom row.

The symbols '.' denotes free space, '#' denotes an obstacle, and '*' denotes part of the shape.
It is guaranteed that the '*' cells are adjacent to each other to form one contiguous shape.

#2024 #interview
"""

def dropBlock2(board):
    """
    Time complexity:
    O(m * n^2) worst case (top half of the board is all '*')
    """
    n, m = len(board), len(board[0])
    move = 0
    result = 0

    for i in reversed(range(n)):
        move += 1
        if "*" in board[i]:
            break

    for i in range(n):
        for j in range(m):
            if board[i][j] != "*":
                continue

            for ii in range(i, i + move):
                if board[ii][j] != "#":
                    continue

                board[ii][j] = "."
                result += 1

    return result


def dropBlock(board):
    """
    Adding visited array prevents redundant cell checking

    Time complexity:
    O(m * n)
    """
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    move = 0
    result = 0

    for i in reversed(range(n)):
        move += 1
        if "*" in board[i]:
            break

    # Process the board from bottom to top so obstacle check doesn't terminate prematurely
    for i in reversed(range(n)):
        for j in range(m):
            if board[i][j] != "*":
                continue

            for ii in range(i, i + move):
                if visited[ii][j] == True:
                    # NOTE: debugging
                    # print(f"terminate cell ({i}, {j}) check, reached cell ({ii}, {j})")
                    break

                visited[ii][j] = True

                if board[ii][j] != "#":
                    continue

                board[ii][j] = "."
                result += 1

                # NOTE: debugging
                # print("\n" + "\n".join(" ".join(row) for row in board))

    return result


if __name__ == "__main__":
    board = [
        ["#", "#", "#", "#", "#"],
        ["#", "*", "*", "*", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#"],
        [".", ".", ".", ".", "."]
    ]
    print(dropBlock(board))  # 6

    board = [
        ["#", "#", "#"],
        ["*", "#", "*"],
        ["*", "#", "*"],
        ["*", "*", "*"],
        ["#", "#", "#"],
        [".", "#", "."]
    ]
    print(dropBlock(board))  # 4

    board = [
        ["#", "#"],
        ["*", "#"]
    ]
    print(dropBlock(board))  # 0

    board = [
        [".", "*", "#"],
        ["*", "*", "*"],
        ["*", "#", "*"],
        ["*", "*", "#"],
        ["#", ".", "#"],
        [".", ".", "#"],
        [".", ".", "#"]
    ]
    print(dropBlock(board))  # 5
