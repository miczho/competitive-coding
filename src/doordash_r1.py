"""
Problem Statement:
You are given a 2D grid representing a city map. Each cell in the grid can be one of the following:
'.' representing an open road that can be traveled.
'X' representing a roadblock that cannot be passed.
'M' representing a market.

You are also given a list of location coordinates within the grid. For each location, your task is to find and return the shortest distance to any market ('M').
The distance is measured in terms of the number of steps taken along the grid cells (up, down, left, right).
If a market cannot be reached from a given location due to roadblocks, return -1 for that location.

Input:
A 2D list grid of size n x m, where grid[i][j] is either '.', 'X', or 'M'.
A list of locations, where each pair [x, y] represents the coordinates of a location in the grid.

Output:
A list of integers, where each integer represents the shortest distance from the corresponding location in the input list to any market. If no market can be reached, return -1 for that location.

Input:
grid = [
    ['.', '.', '.', 'X', 'M'],
    ['.', 'X', '.', '.', '.'],
    ['.', 'M', 'X', '.', 'M'],
    ['.', '.', '.', '.', 'X'],
    ['M', '.', '.', 'X', 'X']
]
locations = [[0, 0], [1, 3], [200, 200], [0, 4], [4, 3], [4, 4]]

Output: [3, 2, -1, 0, 3, -1]



Time Complexity:
O(N*M + N*M + L)
= O(N*M + L)

Space Complexity:
O(N*M + N*M + L)
= O(N*M + L)

Where N = length of 'grid', M = width of 'grid', and L = length of 'locations'

#interview #favorite #bfs #2024
"""

from collections import defaultdict

def findMarketDist(grid, locations):
    n = len(grid)
    m = len(grid[0])
    result = []
    dist = defaultdict(lambda: -1)
    queue = []
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "M":
                queue.append((i, j))
                dist[(i, j)] = 0

    for i, j in queue:
        if grid[i][j] == "X":
            continue

        for iDiff, jDiff in moves:
            iNew, jNew = i + iDiff, j + jDiff

            if 0 <= iNew < n and 0 <= jNew < n and (iNew, jNew) not in dist:
                dist[(iNew, jNew)] = dist[(i, j)] + 1
                queue.append((iNew, jNew))

    for i, j in locations:
        result.append(dist[(i, j)])

    return result



"""
Follow-up Question:
What if, instead of returning the shortest distance to a market, you wanted to return the location(s) of the closest market(s)?

Input:
grid = [
    ['.', '.', '.', 'X', 'M'],
    ['.', 'X', '.', '.', '.'],
    ['.', 'M', 'X', '.', 'M'],
    ['.', '.', '.', '.', 'X'],
    ['M', '.', '.', 'X', 'X']
]
locations = [[0, 0], [1, 3], [200, 200], [0, 4], [4, 3], [4, 4]]

Output:
[
    [[2, 1]],
    [[0, 4], [2, 4]],
    [],
    [[0, 4]],
    [[2, 4], [4, 0]],
    []
]
"""

def findMarketDist2(grid, locations):
    n = len(grid)
    m = len(grid[0])
    result = []
    dist = defaultdict(lambda: float("inf"))
    closestTo = defaultdict(lambda: set())
    queue = []
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "M":
                queue.append((i, j))
                dist[(i, j)] = 0
                closestTo[(i, j)].add((i, j))

    for i, j in queue:
        if grid[i][j] == "X":
            continue

        for iDiff, jDiff in moves:
            iNew, jNew = i + iDiff, j + jDiff

            if 0 <= iNew < n and 0 <= jNew < n:
                if dist[(i, j)] + 1 > dist[(iNew, jNew)]:
                    continue

                dist[(iNew, jNew)] = dist[(i, j)] + 1
                closestTo[(iNew, jNew)].update(closestTo[(i, j)])
                queue.append((iNew, jNew))

    for i, j in locations:
        result.append(closestTo[(i, j)])

    return result

def main():
    grid1 = [
        ['.', '.', '.', 'X', 'M'],
        ['.', 'X', '.', '.', '.'],
        ['.', 'M', 'X', '.', 'M'],
        ['.', '.', '.', '.', 'X'],
        ['M', '.', '.', 'X', 'X']
    ]
    locations1 = [[0, 0], [1, 3], [200, 200], [0, 4], [4, 3], [4, 4]]

    # Expected 0utput: [3, 2, -1, 0, 3, -1]
    print(findMarketDist(grid1, locations1))

    # Expected output:
    # [
    #     [[2, 1]],
    #     [[0, 4], [2, 4]],
    #     [],
    #     [[0, 4]],
    #     [[2, 4], [4, 0]],
    #     []
    # ]
    # print(findMarketDist2(grid1, locations1))

if __name__ == "__main__":
    main()
