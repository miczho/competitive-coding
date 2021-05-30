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
    static final int MAXN = 200_200;
    static int n;
    static int[] u = new int[MAXN];
    static int[] s = new int[MAXN];

    public static void berlandRegional() {
        List<Long>[] school = new List[n];
        for(int i = 0; i < n; i++)
            school[i] = new ArrayList<Long>();

        for(int i = 0; i < n; i++)
            school[u[i] - 1].add((long)(s[i]));

        for(int i = 0; i < n; i++) {
            Collections.sort(school[i], Collections.reverseOrder());
            for(int j = 1; j < school[i].size(); j++) {
                school[i].set(j, school[i].get(j-1) + school[i].get(j));
            }
        }

        long[] res = new long[n];
        for(int i = 0; i < n; i++) {
            List<Long> tmp = school[i];
            for(int j = 1; j <= tmp.size(); j++) {
                res[j-1] += tmp.get((tmp.size() / j * j) - 1);
            }
        }

        for(long i : res)
            System.out.print(i + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        int t = sc.nextInt();

        while(t-- > 0) {
            n = sc.nextInt();
            for(int i = 0; i < n; i++)
                u[i] = sc.nextInt();
            for(int i = 0; i < n; i++)
                s[i] = sc.nextInt();

            berlandRegional();
        }
    }

}