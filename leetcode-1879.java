import java.util.*;
import java.lang.*;

class Solution {
    static int n;
    static int[] dp;
    static int[] a;
    static int[] b;

    public static int dfs(int pos, int mask) {
        if(pos == n) return 0;

        if(dp[mask] == -1) {
            int ans = Integer.MAX_VALUE;
            for(int i = 0; i < n; i++) {
                if(((mask >> i) & 1) == 0) {
                    ans = Math.min(ans, (a[pos] ^ b[i]) + dfs(pos+1, mask | (1 << i)));
                }
            }
            dp[mask] = ans;
        }

        return dp[mask];
    }

    public int minimumXORSum(int[] nums1, int[] nums2) {
        a = nums1; b = nums2;
        n = nums2.length;
        dp = new int[1 << n];
        Arrays.fill(dp, -1);

        return dfs(0, 0);
    }
}