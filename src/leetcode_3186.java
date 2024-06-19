/**
 * Time Complexity:
 * O(N + NlogN + NlogN)
 * = O(NlogN) where N = length of 'power'
 * 
 * Space Complexity:
 * O(N + N)
 * = O(N) where N = length of 'power'
 * 
 * https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
 * 
 * #2024
 */

import java.util.Arrays;

class Solution {
    public long maximumTotalDamage(int[] power) {
        int n = power.length;
        // O(N) space
        int[] processedPower = new int[n + 1];
        // dp[i][0] stores max damage after selecting power[i]
        // dp[i][1] stores max damage up to i-th index
        // O(N) space
        long[][] dp = new long[n + 1][2];
        long result = 0;

        // sentinel value
        processedPower[0] = Integer.MIN_VALUE;
        // O(N) time
        System.arraycopy(power, 0, processedPower, 1, n);
        // O(NlogN) time
        Arrays.sort(processedPower);

        // O(NlogN) time
        for (int i = 1; i < n + 1; i++) {
            if (processedPower[i] == processedPower[i - 1]) {
                // you can greedily cast spells of the same power level
                dp[i][0] = processedPower[i] + dp[i - 1][0];
            } else {
                int lo = 0;
                int hi = i;

                while (lo + 1 != hi) {
                    int mid = lo + (hi - lo) / 2;

                    if (processedPower[mid] < processedPower[i] - 2) {
                        lo = mid;
                    } else {
                        hi = mid;
                    }
                }

                // power of curr spell + max damage of previous usable spells
                dp[i][0] = processedPower[i] + dp[lo][1];
            }

            result = Math.max(result, dp[i][0]);
            dp[i][1] = result;
        }

        return result;
    }
}
