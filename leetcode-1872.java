import java.util.*;
import java.lang.*;

class Solution {
    static final int MAXN = Integer.MAX_VALUE;
    static int n;
    static int[] stones;
    static int[] psum;
    static int[][] dp;

    public static int dfs(int pos, int turn) {
        if(pos == n-1) return (turn == 0) ? psum[pos+1] : -psum[pos+1];

        if(dp[pos][turn] == MAXN) {
            if(turn == 0)
                dp[pos][turn] = Math.max(dfs(pos+1, turn), psum[pos+1] + dfs(pos+1, turn^1));
            else
                dp[pos][turn] = Math.min(dfs(pos+1, turn), -psum[pos+1] + dfs(pos+1, turn^1));
        }

        return dp[pos][turn];
    }

    public static int stoneGameVIII(int[] st) {
        stones = st; n = st.length;

        psum = new int[n+1];
        for(int i = 0; i < n; i++) {
            psum[i+1] = psum[i] + stones[i];
        }

        dp = new int[n][2];
        for(int[] i : dp) Arrays.fill(i, MAXN);

        return dfs(1, 0);
    }
}