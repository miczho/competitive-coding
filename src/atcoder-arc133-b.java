import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static Reader in;
    static Writer out;
    
    // vars
    static int n;
    static int[] p;
    static int[] q;

    public static int dividingSubsequence() {
        int[] posQ = new int[n+1];
        List<List<Integer>> pairs = new ArrayList<List<Integer>>();
        List<Integer> tails = new ArrayList<Integer>();

        for (int i = 0; i < n; i++)
            posQ[q[i]] = i;

        for (int i = 0; i < n; i++) {
            int tmp = 1;
            while (tmp * p[i] <= n) {
                List<Integer> pair = new ArrayList<Integer>();
                pair.add(i);
                pair.add(posQ[tmp * p[i]]);
                pairs.add(pair);
                tmp++;
            }
        }

        Collections.sort(pairs, new Comparator<List<Integer>>() {
            public int compare(List<Integer> l1, List<Integer> l2) {
                int a = l1.get(0) - l2.get(0);
                int b = -(l1.get(1) - l2.get(1));
                return a != 0 ? a : b;
            }
        });

        for (List<Integer> x : pairs) {
            int l = -1, r = tails.size();

            while (l + 1 < r) {
                int m = l + (r - l) / 2;
                if (tails.get(m) >= x.get(1))
                    r = m;
                else
                    l = m;
            }

            if (r == tails.size())
                tails.add(x.get(1));
            else
                tails.set(r, x.get(1));
        }

        return tails.size();
    }

    public static void solve() {
        n = in.nextInt();
        p = new int[n]; q = new int[n];

        for (int i = 0; i < n; i++)
            p[i] = in.nextInt();
        for (int i = 0; i < n; i++)
            q[i] = in.nextInt();

        out.println(dividingSubsequence());
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