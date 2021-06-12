import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static Reader in;
    static Writer out;
    
    // vars
    static final long INF = Long.MAX_VALUE;
    static final int MOD = 1_000_000_007;
    static int n;
    static int[] arr;
    static long[][] dp;
    static long[][] path;

    public static void solve() {
        n = in.nextInt();
        arr = in.readArray(n);

        out.println(manyFormulae());
    }

    public static long manyFormulae() {
        dp = new long[n][2];
        for(long[] i : dp) Arrays.fill(i, INF);
        path = new long[n][2];

        return dfs(0, 0);
    }

    public static long dfs(int pos, int op) {
        if(pos == n-1) {
            path[pos][op] = 1;
            dp[pos][op] = (op == 0) ? arr[pos] : -arr[pos];
        }

        if(dp[pos][op] == INF) {
            long res = 0;
            if(op == 0) {
                res += dfs(pos+1, op);
                path[pos][op] += path[pos+1][op];
                path[pos][op] %= MOD;
            }
            res += dfs(pos+1, op^1);
            path[pos][op] += path[pos+1][op^1];
            path[pos][op] %= MOD;
            res %= MOD;
            res += path[pos][op] * ((op == 0) ? arr[pos] : -arr[pos]);

            dp[pos][op] = res % MOD;
        }

        return dp[pos][op];
    }

    static class Reader {
        BufferedReader br;
        StringTokenizer st;

        public Reader(InputStream stream) {
            br = new BufferedReader(new InputStreamReader(stream));
        }
 
        public Reader(File file) {
            try {
                br = new BufferedReader(new FileReader(file));
            } catch(FileNotFoundException e) {
                e.printStackTrace();
            }
        }
 
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
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
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }

        int[] readArray(int size) {
            int[] a = new int[size];
            for (int i = 0; i < size; i++) a[i] = nextInt();
            return a;
        }
 
        double[] readArrayDouble(int size) {
            double[] a = new double[size];
            for (int i = 0; i < size; i++) a[i] = nextDouble();
            return a;
        }
    }

    static class Writer {
        BufferedWriter bw;
        
        public Writer(OutputStream stream) {
            bw = new BufferedWriter(new OutputStreamWriter(stream));
        }

        public Writer(File file) {
            try {
                bw = new BufferedWriter(new FileWriter(file));
            } catch(IOException e) {
                e.printStackTrace();
            }
        }
        
        void print(Object object) {
            try {
                bw.append("" + object);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        void println(Object object) {
            print(object);
            try {
                bw.append("\n");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        void flush() {
            try {
                bw.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        void close() {
            try {
                bw.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) throws Exception {
        in = new Reader(System.in);
        out = new Writer(System.out);
        
        solve();
        out.close();
    }
}