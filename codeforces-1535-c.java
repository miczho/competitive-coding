import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static Reader in;
    static Writer out;
    
    // vars
    static int n;
    static int[] s;

    public static void solve() {
        int t = in.nextInt();
        while(t-- > 0) {
            char[] tmp = in.next().toCharArray();
            n = tmp.length;
            s = new int[n];
            for(int i = 0; i < n; i++) {
                if(tmp[i] == '1')
                    s[i] = 1;
                else if(tmp[i] == '0') 
                    s[i] = 0;
                else
                    s[i] = -1;
            }

            unstableStr();
        }
    }

    public static void unstableStr() {
        long res = n;

        int turn = 0;
        long val = 0;
        for(int x : s) {
            if(x == turn || x == -1) {
                val++;
            } else {
                res += val * (val-1) / 2;
                val = 0;
            }
            turn ^= 1;
        }
        res += val * (val-1) / 2;

        turn = 1;
        val = 0;
        for(int x : s) {
            if(x == turn || x == -1) {
                val++;
            } else {
                res += val * (val-1) / 2;
                val = 0;
            }
            turn ^= 1;
        }
        res += val * (val-1) / 2;

        val = 0;
        for(int x : s) {
            if(x == -1) {
                val++;
            } else {
                res -= val * (val-1) / 2;
                val = 0;
            }
        }
        res -= val * (val-1) / 2;

        out.println(res);
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