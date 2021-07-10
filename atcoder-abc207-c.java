import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static Reader in;
    static Writer out;

    public static void solve() {
        int n = in.nextInt();
        int[][] arr = new int[n][3];
        for (int i = 0; i < n; i++) {
            arr[i] = in.readArray(3);
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if ((arr[j][1] > arr[i][1] && arr[j][1] < arr[i][2]) 
                    || (arr[j][2] > arr[i][1] && arr[j][2] < arr[i][2])
                    || (arr[i][1] > arr[j][1] && arr[i][1] < arr[j][2])
                    || (arr[i][2] > arr[j][1] && arr[i][2] < arr[j][2])
                    || (arr[i][1] == arr[j][1] && arr[i][2] == arr[j][2]))
                    res++;
                else if ((arr[i][0] == 1 || arr[i][0] == 2) 
                         && (arr[j][0] == 1 || arr[j][0] == 3) 
                         && (arr[i][1] == arr[j][2]))
                    res++;
                else if ((arr[j][0] == 1 || arr[j][0] == 2) 
                         && (arr[i][0] == 1 || arr[i][0] == 3) 
                         && (arr[j][1] == arr[i][2]))
                    res++;
            }
        }

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