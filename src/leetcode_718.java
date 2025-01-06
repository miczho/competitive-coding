/**
 * https://leetcode.com/problems/maximum-length-of-repeated-subarray/
 * 
 * #favorite #dp #slidingWindow #binarySearch
 */

class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length;
        int[] dp = new int[m + 1];
        int result = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = m; j >= 1; j--) {  // Iterate in reverse to prevent overwriting previous dp[j] values
                if (nums1[i - 1] == nums2[j - 1]) {
                    dp[j] = dp[j - 1] + 1;
                    result = Math.max(result, dp[j]);
                } else {
                    dp[j] = 0;  // Reset to zero to ensure no invalid continuation of subarrs
                }
            }
        }

        return result;
    }
}
