/**
 * https://leetcode.com/problems/making-a-large-island/
 * 
 * #2025
 */
import java.util.*;

class Solution {
    private int n, m;
    private int[][] island;
    private int islandId = 1;
    private int[][] moves = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

    public int largestIsland(int[][] grid) {
        this.n = grid.length;
        this.m = grid[0].length;
        this.island = new int[this.n][this.m];
        Map<Integer, Integer> map = new HashMap<>();
        int result = 0;

        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.m; j++) {
                if (grid[i][j] == 0 || this.island[i][j] != 0)
                    continue;

                map.put(this.islandId, this.bfs(grid, i, j));

                result = Math.max(result, map.get(this.islandId));
                this.islandId++;
            }
        }

        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.m; j++) {
                if (grid[i][j] == 1)
                    continue;

                int newResult = 1;
                Set<Integer> set = new HashSet<>();

                for (int[] move : this.moves) {
                    int ii = i + move[0], jj = j + move[1];
                    boolean inBounds = ii >= 0 && ii < this.n && jj >= 0 && jj < this.m;

                    if (inBounds && !set.contains(this.island[ii][jj])) {
                        set.add(this.island[ii][jj]);
                        newResult += map.getOrDefault(this.island[ii][jj], 0);
                    }
                }

                result = Math.max(result, newResult);
            }
        }

        return result;
    }

    public int bfs(int[][] grid, int i, int j) {
        Queue<int[]> queue = new LinkedList<>();
        int islandSize = 0;

        queue.add(new int[] { i, j });
        this.island[i][j] = this.islandId;

        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            int x = node[0], y = node[1];

            islandSize++;

            for (int[] move : this.moves) {
                int xx = x + move[0], yy = y + move[1];
                boolean inBounds = xx >= 0 && xx < this.n && yy >= 0 && yy < this.m;

                if (inBounds && grid[xx][yy] == 1 && this.island[xx][yy] == 0) {
                    queue.add(new int[] { xx, yy });
                    this.island[xx][yy] = this.islandId;
                }
            }
        }

        return islandSize;
    }
}
