import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static int n;
    static int first;
    static int second;
    static int top;
    static int bot;
    
    public static int[] earliestAndLatest(int N, int firstPlayer, int secondPlayer) {
        n = N; first = firstPlayer; second = secondPlayer;
        first--; second--;
        top = Integer.MIN_VALUE; bot = Integer.MAX_VALUE;
        
        dfs(0, 0, n-1, 1);
        return new int[]{bot, top};
    }
    
    public static void dfs(int mask, int i, int j, int round) {
        while(((mask >> i) & 1) == 1) i++;
        while(((mask >> j) & 1) == 1) j--;
                
        if(i == first && j == second) {
            top = Math.max(top, round);
            bot = Math.min(bot, round);
        } else if(i >= j) {
            dfs(mask, 0, n-1, round+1);
        } else {
            if(i != first && i != second)
                dfs(mask | (1 << i), i+1, j-1, round);
            if(j != first && j != second)
                dfs(mask | (1 << j), i+1, j-1, round);
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.earliestAndLatest(11, 2, 4)));
        System.out.println(Arrays.toString(s.earliestAndLatest(17, 1, 2)));
    }
}