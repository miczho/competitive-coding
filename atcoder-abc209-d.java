/*
#dfs #dp #lca #binary-lifting
https://atcoder.jp/contests/abc209/tasks/abc209_d
*/

import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static Reader in;
    static Writer out;
    
    // vars
    static int n, q;
    static List<List<Integer>> children;
    // up[i][j] memoizes the 2^j-th parent of a node
    static int up[][], depth[], log;

    public static void solve() {
        n = in.nextInt();
        q = in.nextInt();

        // building tree
        children = new ArrayList<>();
        for(int i = 0; i < n+1; i++)
            children.add(new ArrayList<>());
        for(int i = 0; i < n-1; i++) {
            int a = in.nextInt();
            int b = in.nextInt();

            children.get(a).add(b);
            children.get(b).add(a);
        }

        // calculating max possible depth and building memory
        log = 0;
        while((1 << (log + 1)) <= n)
            log++;
        up = new int[n+1][log];
        depth = new int[n+1];

        // tree traveral, populating up[][] and depth[]
        dfs(1, 0);

        while(q-- > 0) {
            int c = in.nextInt();
            int d = in.nextInt();

            // shortest path is depth of each node from the root
            // minus the uneeded distance between the root and the lca
            int ancestor = lca(c, d);
            int dist = depth[c] + depth[d] - (2 * depth[ancestor]);

            if((dist & 1) == 1)
                out.println("Road");
            else
                out.println("Town");
        }
    }

    public static void dfs(int node, int parent) {
        for(int i = 1; i < log; i++) {
            // if curr depth is >= 2^i, then calculate the 2^i-th parent of the node
            if(depth[node] >= (1 << i)) {
                // the 2^i-th parent is the 2^(i-1)-th parent of the 2^(i-1)-th parent
                // in other words, 2^i = 2^(i-1) + 2^(i-1)
                int x = up[node][i-1];
                up[node][i] = up[x][i-1];
            }
        }

        for(int child : children.get(node)) if(child != parent) {
            // the 2^0-th parent, aka the 1st parent, of the child is the curr node
            up[child][0] = node;
            // child is one edge deeper than the curr node
            depth[child] = depth[node] + 1;
            dfs(child, node);
        }
    }

    public static int lca(int node1, int node2) {
        if(depth[node1] < depth[node2]) {
            // perform a swap
            node1 ^= node2; 
            node2 ^= node1; 
            node1 ^= node2;
        }

        // jump node1 to the same depth as node2
        int diff = depth[node1] - depth[node2];
        for(int i = 0; i < log; i++) if((diff & (1 << i)) == 1) {
            node1 = up[node1][i];
        }

        // if they point to the same node, the lca has been found
        if(node1 == node2)
            return node1;

        // otherwise, jump both nodes to the point JUST BEFORE the lca...
        for(int i = log-1; i <= 0; i--) if(up[node1][i] != up[node2][i]) {
            node1 = up[node1][i];
            node2 = up[node2][i];
        }
        // ...and the node right above them is the lca
        return up[node1][0];
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