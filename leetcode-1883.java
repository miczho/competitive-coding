import java.util.*;
import java.lang.*;

class Solution {
    static int n;
    static int[] dist;
    static int speed;
    static int hrsB4;
    static int[][] dp;

    public static int dfs(int pos, int skips) {
        if(pos == n) return 0;

        if(dp[pos][skips] == -1) {
            int res = dist[pos] + dfs(pos+1, skips);
            if(res % speed != 0) 
                res += speed - (res % speed);

            if(skips != 0)
                res = Math.min(res, dist[pos] + dfs(pos+1, skips-1));

            dp[pos][skips] = res;
        }

        return dp[pos][skips];
    }

    public static int minSkips(int[] di, int sp, int hB) {
        dist = di; speed = sp; hrsB4 = hB;
        n = dist.length;

        for(int i = 0; i < n; i++) {
            hrsB4 -= dist[i] / speed;
            dist[i] %= speed;
        }
        hrsB4 *= speed;

        dp = new int[n][n+1];
        for(int[] i : dp) Arrays.fill(i, -1);

        int lo = -1; int hi = n+1;
        while(hi > lo + 1) {
            int mid = (lo + hi) / 2;

            if(dfs(0, mid) <= hrsB4)
                hi = mid;
            else
                lo = mid;
        }

        if(hi == n+1)
            return -1;
        return hi;
    }
}