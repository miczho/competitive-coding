/**
 * https://leetcode.com/problems/alice-and-bob-playing-flower-game/
 */

class Solution {
    public long flowerGame(int n, int m) {
        // all possible sums = n * m
        // even & even, odd & odd, odd & even, even & odd
        // all possible odd sums = n * m / 2
        return (long) n * m / 2;
    }
}