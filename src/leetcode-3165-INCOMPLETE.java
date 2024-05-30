/*
This initial soln with pure DP does not work bc I read the problem wrong.
After a query is completed, nums[] is modified PERMANENTLY.
This condition makes the problem more complex, you need add use of either segment tree or square root decomposition to solve it.

https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

#2024
*/

import java.util.HashMap;

class Solution {
    public static final int MOD = (int) Math.pow(10, 9) + 7;

    private HashMap<String, Integer> memo;
    private int[] nums;

    public int maximumSumSubsequence(int[] nums, int[][] queries) {
        this.memo = new HashMap<>();
        this.nums = nums;

        int n = nums.length;

        int result = 0;
        for (int[] q : queries) {
            result += Math.max(
                // case where you don't select nums[q[0]]
                (this.findSum(0, q[0]) + this.findSum(q[0] + 1, n)) % MOD,
                // case where you do select nums[q[0]]
                (this.findSum(0, q[0] - 1) + q[1] + this.findSum(q[0] + 2, n)) % MOD
            );
            result %= MOD;
        }

        return result;
    }

    public int findSum(int lo, int hi) {
        // return 0 once the range is empty
        if (lo >= hi) {
            return 0;
        }

        String key = lo + "," + hi;
        
        // calculate and store value
        if(this.memo.containsKey(key) == false) {
            if (this.nums[lo] > 0) {
                // if nums[lo] is positive, we COULD select it
                this.memo.put(
                    key,
                    Math.max(
                        this.findSum(lo + 1, hi) % MOD,
                        (this.nums[lo] + this.findSum(lo + 2, hi)) % MOD
                    )
                );
            } else {
                // otherwise we don't select it
                this.memo.put(
                    key,
                    this.findSum(lo + 1, hi) % MOD
                );
            }
        }

        return this.memo.get(key);
    }
}