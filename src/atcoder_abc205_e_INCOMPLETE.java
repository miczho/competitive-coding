import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static Reader in;
    static Writer out;
    
    // vars
    static final int MOD = 1_000_000_007;
    static int n;
    static int w;
    static int b;
    static int k;
    static int[] fac;
    static int[] inv;

    public static void solve() {
        w = in.nextInt();
        b = in.nextInt();
        k = in.nextInt();
        n = w + b;

        fac = new int[n+1]; inv = new int[n+1];
        fac[0] = 1; inv[0] = 1;
        for(int i = 1; i <= n; i++) {
            fac[i] = (int)(fac[i-1] * (long)(i) % MOD);
            inv[i] = pow(fac[i], MOD-2);
        }
        
        out.println(whiteBlackBalls());
    }

    public static int pow(int x, int y) {
        if(y == 1) return x;

        if(y%2 == 1)
            return (int)((long)(1) * x * pow(x, y-1) % MOD);
        int res = pow(x, y/2);
        return (int)((long)(1) * res * res % MOD);
    }

    public static int nCr(int N, int R) {
        if(N < R) return 0;
        return (int)((long)(1) * fac[N] * inv[R] % MOD * inv[N-R] % MOD);
    }

    public static int whiteBlackBalls() {
        if(w > b + k) return 0;
        return nCr(n, b) - nCr(n, b+k+1);
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