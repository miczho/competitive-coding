import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.lang.*;

class Main {
    // vars
    static int n;
    static int[][] arr;

    public static void dfs(int c, int val, int i, int j) {
        if(c <= 0)
            return;
        arr[i][j] = val;
        if((j-1) >= 0 && arr[i][j-1] == 0)
            dfs(c-1, val, i, j-1);
        else
            dfs(c-1, val, i+1, j);
    }

    public static void fillomino2() {
        for(int i = 0; i < n; i++)
            dfs(arr[i][i], arr[i][i], i, i);

        for(int i = 0; i < n; i++) {
            for(int j = 0; j <= i; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        n = sc.nextInt();
        arr = new int[n][n];
        for(int i = 0; i < n; i++)
            arr[i][i] = sc.nextInt();

        fillomino2();
    }

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
}