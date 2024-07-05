/**
 * https://neetcode.io/problems/missing-number
 * 
 * #2024
 */

class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int result = 0;

        for (int i = 0; i < n; i++) {
            result += i + 1;
            result -= nums[i];
        }

        return result;
    }
}
