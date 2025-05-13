/**
 * https://leetcode.com/problems/word-search/
 * 
 * #2025 #payPal
 */


/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  const m = board.length
  const n = board[0].length
  const wordLen = word.length
  const visited = []
  const move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

  for (let i = 0; i < m; i++) {
    visited.push(new Array(n).fill(false))
  }

  let dfs = (x, y, wordIdx) => {
    if (board[x][y] !== word[wordIdx]) {
      return false
    } else if (wordIdx === wordLen - 1) {
      return true
    }

    visited[x][y] = true
    for (let i = 0; i < 4; i++) {
      const xNew = x + move[i][0]
      const yNew = y + move[i][1]
      const inBounds = xNew >= 0 && xNew < m && yNew >= 0 && yNew < n

      if (inBounds && !visited[xNew][yNew]) {
        if (dfs(xNew, yNew, wordIdx + 1) === true) {
          return true
        }
      }
    }
    visited[x][y] = false

    return false
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (dfs(i, j, 0) === true) {
        return true
      }
    }
  }

  return false
};
