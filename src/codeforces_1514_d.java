/**
 * #incomplete
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
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
    static final int MAXN = 300_300;
    static int n;
    static int q;
    static int[] arr = new int[MAXN];
    static List<Integer>[] sets;
    static int[] rand = new int[25];

    static PrintWriter out;

    public static int bin(int pick, int val) {
        List<Integer> num_freq = sets[pick];
        // System.out.println(pick);

        int lo = -1; 
        int hi = num_freq.size();
        while(hi > lo + 1) {
            int mid = (lo + hi) / 2;
            if(num_freq.get(mid) <= val) {
                lo = mid;
            } else {
                hi = mid;
            }
        }

        return lo;
    }

    public static int cutAndStick(int l, int r) {
        int max_freq = (r - l + 2) / 2;
        int[] picks = new int[25];

        for(int i=0; i<25; i++) {
            int tmp = rand[i] % (r - l + 1) + l;
            picks[i] = arr[tmp];
        }
 
        for(int i=0; i<25; i++) {
            int lower = bin(picks[i], l-1);
            int upper = bin(picks[i], r);
            if(upper - lower > max_freq) {
                return 2 * (upper - lower) - r + l - 1;
            }
        }
 
        return 1;
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        out = new PrintWriter(new OutputStreamWriter(System.out));

        n = sc.nextInt();
        q = sc.nextInt();
        sets = new Vector[n+1];
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            sets[i+1] = new Vector<>();
        }

        for(int i = 0; i < n; i++) sets[arr[i]].add(i);

        for(int i = 0; i < 25; i++) rand[i] = (int)(Math.random() * 3 * 1000000);

        while(q-- > 0) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            l--; r--;

            out.println(cutAndStick(l, r));
        }
        out.flush();
        out.close();
    }

}