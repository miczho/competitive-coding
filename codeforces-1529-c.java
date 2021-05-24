import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.lang.*;

class Main {
    static int MAXN = 100_100;
    static int[][] bound = new int[MAXN][2];
    static List<Integer>[] childs = new ArrayList[MAXN];
    static long[][] dp = new long[MAXN][2];

    public static void humongousTree(int prev, int curr) {
        if(dp[curr][0] == -1) {
            long hi = 0; long lo = 0;
            for(int child : childs[curr]) {
                if(child != prev) {
                    humongousTree(curr, child);
                    lo += Math.max(Math.abs(bound[curr][0] - bound[child][0]) + dp[child][0], Math.abs(bound[curr][0] - bound[child][1]) + dp[child][1]);
                    hi += Math.max(Math.abs(bound[curr][1] - bound[child][0]) + dp[child][0], Math.abs(bound[curr][1] - bound[child][1]) + dp[child][1]);
                }
            }
            dp[curr][0] = lo;
            dp[curr][1] = hi;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tk = new StringTokenizer(in.readLine());
        int t = Integer.parseInt(tk.nextToken());

        while(t-- > 0) {
            tk = new StringTokenizer(in.readLine());
            int n = Integer.parseInt(tk.nextToken());
            for(int i = 0; i < n; i++) {
                tk = new StringTokenizer(in.readLine());
                bound[i][0] = Integer.parseInt(tk.nextToken());
                bound[i][1] = Integer.parseInt(tk.nextToken());
            }

            for(int i = 0; i < n; i++)
                childs[i] = new ArrayList<Integer>();

            for(int i = 0; i < n - 1; i++) {
                tk = new StringTokenizer(in.readLine());
                int u = Integer.parseInt(tk.nextToken());
                int v = Integer.parseInt(tk.nextToken());
                u--; v--;
                childs[u].add(v);
                childs[v].add(u);
            }

            for(long[] i : dp)
                Arrays.fill(i, -1);

            humongousTree(-1, 0);
            System.out.println(Math.max(dp[0][0], dp[0][1]));
        }
    }
}