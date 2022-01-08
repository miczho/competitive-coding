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
    static String s;

    public static long arrangingSheep() {
        List<Integer> sheep = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            if(s.charAt(i) == '*') sheep.add(i);
        }
        if(sheep.isEmpty()) return 0;

        long res = 0;
        int x = sheep.size() / 2;
        int mid = sheep.get(sheep.size() / 2);
        while(x >= 0) {
            res += mid - sheep.get(x);
            mid--; x--;
        }

        x = sheep.size() / 2;
        mid = sheep.get(sheep.size() / 2);
        while(x < sheep.size()) {
            res += sheep.get(x) - mid;
            mid++; x++;
        }

        return res;
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        int t = sc.nextInt();

        while(t-- > 0) {
            n = sc.nextInt();
            s = sc.next();

            System.out.println(arrangingSheep());
        }
    }
}