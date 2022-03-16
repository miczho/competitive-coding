import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static Reader in;
    static Writer out;
    
    // vars
    static int m, n;
    static int dp[][] = new int[3050][3050];

    public static int dfs(String cipher, String target, int i, int j) {
        if (i == m || j == n) return 0;

        if (dp[i][j] == -1) {
            if (cipher.charAt(i) != target.charAt(j))
                dp[i][j] = Math.max(dfs(cipher, target, i+1, j), dfs(cipher, target, i, j+1));
            else
                dp[i][j] = 1 + dfs(cipher, target, i+1, j+1);
        }

        return dp[i][j];
    }

    public static int dfs(String cipher, String target) {
        for (int[] row: dp)
            Arrays.fill(row, -1);
        return dfs(cipher, target, 0, 0);
    }

    public static String genCipher(String source, int key) {
        char res[] = new char[m];

        for (int i = 0; i < m; i++) {
            int new_ch = (int)(source.charAt(i)) + key;
            if (new_ch > (int)('z')) new_ch -= 26;
            res[i] = (char)(new_ch);
        }

        return new String(res);
    }

    public static int editDistance(String source, String target) {
        m = source.length(); n = target.length();
        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < 26; i++) {
            String cipher = genCipher(source, i);
            int common = dfs(cipher, target);
            ans = Math.min(ans, m + n - 2 * common);
        }

        return ans;
    }

    public static void solve() {
        String source = in.next();
        String target = in.next();

        out.println(editDistance(source, target));
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
 
        long[] readArrayLong(int size) {
            long[] a = new long[size];
            for (int i = 0; i < size; i++) a[i] = nextLong();
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