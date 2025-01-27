/**
 * https://leetcode.com/problems/random-pick-with-weight/
 * 
 * #2025
 */

import java.util.Random;

class Solution {
    /**
     * Time complexity:
     * O(nlogn)
     * 
     * Space complexity:
     * O(n)
     * 
     * Where n = w.length = 10^4
     */

    private Random rand;
    private int[] prefixSum;

    public Solution(int[] w) {
        this.rand = new Random();
        this.prefixSum = new int[w.length];

        this.prefixSum[0] = w[0];
        for (int i = 1; i < w.length; i++) {
            this.prefixSum[i] = w[i] + this.prefixSum[i - 1];
        }
    }

    public int pickIndex() {
        int total = this.prefixSum[this.prefixSum.length - 1];
        int val = this.rand.nextInt(total) + 1;

        int lo = -1, hi = this.prefixSum.length;
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;

            if (val <= this.prefixSum[mid]) {
                hi = mid;
            } else {
                lo = mid;
            }
        }

        return hi;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
