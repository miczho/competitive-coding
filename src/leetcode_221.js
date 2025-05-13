/**
 * https://leetcode.com/problems/maximal-square/
 * 
 * #2025 #payPal
 */


/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function (matrix) {
  const m = matrix.length
  const n = matrix[0].length
  const memo = {}
  let maxSize = 0

  const dfs = (x, y) => {
    if (x >= m || y >= n) {
      return 0
    } else if (matrix[x][y] === "0") {
      return 0
    } else if ([x, y] in memo) {
      return memo[[x, y]]
    }

    memo[[x, y]] = 1 + Math.min(
      dfs(x + 1, y),
      dfs(x, y + 1),
      dfs(x + 1, y + 1)
    )

    return memo[[x, y]]
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      maxSize = Math.max(maxSize, dfs(i, j))
    }
  }

  return Math.pow(maxSize, 2)
};