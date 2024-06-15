import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.lang.*;

class Solution {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
 
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
 
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt() { return Integer.parseInt(next()); }
 
        long nextLong() { return Long.parseLong(next()); }
 
        double nextDouble() { return Double.parseDouble(next()); }
 
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
    
    // vars
    static int t;
    static int x;
    static int w;
    static int e;
    static double[][][] dp = new double[60][60][60];
    static int[][][][] next = new int[60][60][60][3];

    public static double dfs(int r, int p, int s) {
        int round = r + p + s;

        if(round == 60) return 0;

        if(dp[r][p][s] == -1) {
            double r_freq = 1.0/3; double p_freq = 1.0/3; double s_freq = 1.0/3;
            if(round != 0) {
                r_freq = (double)(s)/round; p_freq = (double)(r)/round; s_freq = (double)(p)/round;
            }

            double res = (e * r_freq) + (w * s_freq) + dfs(r+1, p, s);
            next[r][p][s] = new int[]{r+1, p, s};
            double tmp = (e * p_freq) + (w * r_freq) + dfs(r, p+1, s);
            if(res < tmp) {
                res = tmp;
                next[r][p][s] = new int[]{r, p+1, s};
            }
            tmp = (e * s_freq) + (w * p_freq) + dfs(r, p, s+1);
            if(res < tmp) {
                res = tmp;
                next[r][p][s] = new int[]{r, p, s+1};
            }

            dp[r][p][s] = res;
        }

        return dp[r][p][s];
    }

    public static String build() {
        int r = 0; int p = 0; int s = 0;
        char[] res = new char[60];

        for(int i = 0; i < 60; i++) {
            int[] tmp = next[r][p][s];
            if(r < tmp[0]) {
                res[i] = 'R';
                r += 1;
            }
            else if(p < tmp[1]) {
                res[i] = 'P';
                p += 1;
            }
            else {
                res[i] = 'S';
                s += 1;
            }
        }

        return new String(res);
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        t = sc.nextInt(); x = sc.nextInt();

        for(int i = 0; i < t; i++) {
            w = sc.nextInt();
            e = sc.nextInt();
            for(double[][] j : dp) for(double[] k : j) Arrays.fill(k, -1);
            dfs(0, 0, 0);
            System.out.println(String.format("Case #%d: %s", i+1, build()));
        }
    }

}