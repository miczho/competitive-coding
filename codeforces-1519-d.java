import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.lang.*;

class Main {
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
    static int n;
    static long[] a; 
    static long[] b;

    public static void maxSumProducts() {
        long[] dp = new long[n+1];
        for(int i = 0; i < n; i++) {
            dp[i+1] = dp[i] + (a[i] * b[i]);
        }

        long ans = dp[n];
        for(int i = 0; i < n; i++) {
            long tmp = a[i] * b[i];
            int j = i-1;
            int k = i+1;
            while(j >= 0 && k < n) {
                tmp += a[k] * b[j];
                tmp += a[j] * b[k];
                ans = Math.max(ans, tmp + dp[j] + (dp[n] - dp[k+1]));
                j--; k++;
            }

            tmp = 0;
            j = i;
            k = i+1;
            while(j >= 0 && k < n) {
                tmp += a[k] * b[j];
                tmp += a[j] * b[k];
                ans = Math.max(ans, tmp + dp[j] + (dp[n] - dp[k+1]));
                j--; k++;
            }
        }

        System.out.println(ans);
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        n = sc.nextInt();
        a = new long[n]; b = new long[n];
        for(int i = 0; i < n; i++)
            a[i] = sc.nextLong();
        for(int i = 0; i < n; i++)
            b[i] = sc.nextLong();

        maxSumProducts();
    }
}