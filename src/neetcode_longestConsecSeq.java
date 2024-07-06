/**
 * https://neetcode.io/problems/longest-consecutive-sequence
 * 
 * #2024
 */

class Solution {
    public int longestConsecutive(int[] nums) {
        int target = Integer.MIN_VALUE;
        int cnt = 1;
        int result = 0;

        Arrays.sort(nums);

        for (int num : nums) {
            if (num == target) {
                target++;
                cnt++;
            } else if (num == target - 1) {
                continue;
            } else {
                target = num + 1;
                cnt = 1;
            }
            result = Math.max(result, cnt);
        }

        return result;
    }
}
