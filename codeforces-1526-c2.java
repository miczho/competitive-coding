import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader(InputStream stream) {
            br = new BufferedReader(new InputStreamReader(stream));
        }
 
        public FastReader(File file) {
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
    }
    
    // vars
    static final int MAXN = 200_200;
    static int n;
    static int[] arr = new int[MAXN];

    public static void potionsII() {
        long health = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>(n);

        for(int i = 0; i < n; i++) {
            if(health + arr[i] >= 0) {
                health += arr[i];
                q.add(arr[i]);
            } else {
                if(!q.isEmpty() && q.peek() < arr[i]) {
                    health -= q.poll();
                    health += arr[i];
                    q.add(arr[i]);
                }
            }
        }

        System.out.println(q.size());
    }

    public static void main(String[] args) throws IOException {
        FastReader in = new FastReader(System.in);

        n = in.nextInt();
        for(int i = 0; i < n; i++) 
            arr[i] = in.nextInt();

        potionsII();
    }

}