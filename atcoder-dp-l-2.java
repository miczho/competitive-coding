/*
player1 tries to MAXIMIZE score(player1) - score(player2)
player2 tries to MINIMIZE score(player1) - score(player2)
THIS IS THE TOP DOWN SOLUTION
#minimax
*/

import java.util.*;

class Main {
	private static final long INF = Long.MAX_VALUE;
	private int n;
	private long[] arr;
	private long[][][] dp;

	public Main(int n, long[] arr) {
		this.n = n;
		this.arr = arr;
		this.dp = new long[n][n][2];
		for(long[][] i : this.dp) for(long[] j : i) Arrays.fill(j, INF);
	}

	public long dequeGame(int i, int j, int k) {
		if(i > j)
			return 0;

		// the minimizing and maximizing alternate depending on whose turn it is
		if(dp[i][j][k] == INF) {
			long a = dequeGame(i+1, j, k^1) + arr[i] * ((k == 1)?-1:1);
			long b = dequeGame(i, j-1, k^1) + arr[j] * ((k == 1)?-1:1);
			dp[i][j][k] = (k == 1) ? Math.min(a, b) : Math.max(a, b);
		}

		return dp[i][j][k];
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] arr = new long[n];
		for(int i=0; i < n; i++)
			arr[i] = sc.nextLong();
		
		Main sol = new Main(n, arr);
		System.out.println(sol.dequeGame(0, n-1, 0));
	}
}