import java.util.*;
import java.lang.*;

class Solution {
    static final int MOD = 1_000_000_007;
    static int n;
    static int k;
    static long[][] dp;

    public static long dfs(int num, int chose) {
        if(num < chose || chose == 0) return 0;
        if(num == chose) return 1;

        if(dp[num][chose] == -1) {
            long res = dfs(num-1, chose-1) % MOD;
            res += (num - 1) * dfs(num-1, chose) % MOD;

            dp[num][chose] = res % MOD;
        }

        return dp[num][chose];
    }

    public static int rearrangeSticks(int nn, int kk) {
        n = nn; k = kk;

        dp = new long[1010][1010];
        for(long[] i : dp) Arrays.fill(i, -1);

        return (int)(dfs(n, k));
    }
}