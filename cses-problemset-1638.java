import java.util.*;

class Main {
    private static final long INF = Long.MAX_VALUE;
    private int n;
    private String[] arr;
    private long[][] dp;

    public Main(int n, String[] arr) {
        this.n = n;
        this.arr = arr;
        this.dp = new long[n][n];
        for(long[] i : this.dp) Arrays.fill(i, INF);
    }

    public long gridPaths(int x, int y) {
        if(x == this.n-1 && y == this.n-1)
            return 1;

        if(dp[x][y] == INF) {
            long ans = 0;
            if(x+1 < n && arr[x+1].charAt(y) == '.') {
                ans += gridPaths(x+1, y) % 1_000_000_007;
            }
            if(y+1 < n && arr[x].charAt(y+1) == '.') {
                ans += gridPaths(x, y+1) % 1_000_000_007;
            }
            dp[x][y] = ans % 1_000_000_007;
        }

        return dp[x][y];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        String[] arr = new String[n];
        for(int i=0; i < n; i++)
            arr[i] = sc.nextLine();
        
        Main sol = new Main(n, arr);
        if(arr[0].charAt(0) == '*') {
            System.out.println(0);
        } else {
            System.out.println(sol.gridPaths(0, 0));
        }
        sc.close();
    }
}