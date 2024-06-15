/**
 * colors map keeps a count of balls of the same color
 * balls map keeps the color of one ball
 * for each query, remove ball from its old count if necessary, then add the ball to its updated color
 * result is the current size of the colors map
 * 
 * Time Complexity:
 * O(N) where N = length of 'queries'
 * 
 * Space Complexity:
 * O(N + N + N)
 * = O(N) where N = length of 'queries'
 * 
 * https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/
 * 
 * #2024
 */

import java.util.HashMap;

class Solution {
    private int n;

    public int[] queryResults(int limit, int[][] queries) {
        this.n = queries.length;

        // O(N) space
        Map<Integer,Integer> colors = new HashMap<>();
        // O(N) space
        Map<Integer,Integer> balls = new HashMap<>();
        // O(N) space
        int[] result = new int[n];

        // O(N) time
        for (int i = 0; i < n; i++) {
            int ball = queries[i][0];
            int color = queries[i][1];

            // remove old color
            if (balls.containsKey(ball)) {
                int oldColor = balls.get(ball);
                int newColorCount = colors.get(oldColor) - 1;

                if (newColorCount == 0) {
                    colors.remove(oldColor);
                } else {
                    colors.put(oldColor, newColorCount);
                }
            }

            // add new color
            balls.put(ball, color);
            colors.put(color, colors.getOrDefault(color, 0) + 1);

            result[i] = colors.size();
        }

        return result;
    }
}
