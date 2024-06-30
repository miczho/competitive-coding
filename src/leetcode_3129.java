/**
 * Try to find a simpler solution.
 * 
 * https://leetcode.com/problems/find-all-zerosible-stable-binary-arrays-i/
 * 
 * #2024 #revisit
 */

class Solution {
    final static int MOD = 1_000_000_007;

    int[][][] dp;

    public int numberOfStableArrays(int zero, int one, int limit) {
        dp = new int[zero + 1][one + 1][2];

        for (int i = 0; i <= Math.min(zero, limit); i++) {
            dp[i][0][0] = 1;
        }
        for (int j = 0; j <= Math.min(one, limit); j++) {
            dp[0][j][1] = 1;
        }

        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                dp[i][j][0] = (sum(getDp(i - 1, j)) + MOD - getDp(i - limit - 1, j, 1)) % MOD;
                dp[i][j][1] = (sum(getDp(i, j - 1)) + MOD - getDp(i, j - limit - 1, 0)) % MOD;
            }
        }

        return sum(dp[zero][one]) % MOD;
    }

    int[] getDp(int zero, int one) {
        int[] result = (zero >= 0 &&
                        zero < dp.length &&
                        one >= 0 &&
                        one < dp[0].length) ? dp[zero][one] : new int[2];
        return result;
    }

    int getDp(int zero, int one, int val) {
        int result = (zero >= 0 &&
                      zero < dp.length &&
                      one >= 0 &&
                      one < dp[0].length) ? dp[zero][one][val] : 0;
        return result;
    }

    static int sum(int[] arr) {
        int result = 0;
        for (int x : arr) {
            result += x;
            result %= MOD;
        }
        return result;
    }
}
