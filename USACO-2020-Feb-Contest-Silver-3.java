import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
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
    static final int MAXN = 150;
    static int n;
    static int[] clock;
    static int[] copy;
    static List<List<Integer>> g = new ArrayList<List<Integer>>(MAXN);

    public static int dfs(int prev, int node) {
        List<Integer> childs = g.get(node);
        for(int i = 0; i < childs.size(); i++) {
            if(childs.get(i) == prev) continue;
            copy[node] += dfs(node, childs.get(i));
            copy[node] %= 12;
        }

        return 12 - copy[node];
    }

    public static int dfsDriver(int node) {
        List<Integer> childs = g.get(node);
        for(int i = 0; i < childs.size(); i++) {
            copy[node] += dfs(node, childs.get(i));
            copy[node] %= 12;
        }

        return copy[node];
    }

    public static void clockTree() throws IOException {
        int res = 0;
        // PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("clocktree.out")));
        for(int i = 0; i < n; i++) {
            copy = Arrays.copyOf(clock, clock.length);
            if(dfsDriver(i) < 2) res++;
        }

        // out.print(res);
        // out.close();
        System.out.println(res);
    }

    public static void main(String[] args) throws IOException {
        // File file = new File("clocktree.in");
        // FastReader sc = new FastReader(file);
        FastReader sc = new FastReader(System.in);
        n = sc.nextInt();
        clock = new int[n];
        for(int i = 0; i < n; i++) {
            clock[i] = sc.nextInt() % 12;
            g.add(new ArrayList<Integer>());
        }

        for(int i = 0; i < n-1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            u--; v--;
            g.get(u).add(v);
            g.get(v).add(u);
        }

        clockTree();
    }
}