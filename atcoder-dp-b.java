import java.util.*;

class Main {
    public static int frog(int[] h, int n, int k) {
    	int[] dp = new int[n];

    	for(int i = 1; i < n; i++) {
    		dp[i] = dp[i-1] + Math.abs(h[i] - h[i-1]);
    		for(int j = 2; j <= k; j++) {
    			if(j > i) break;
    			dp[i] = Math.min(dp[i], dp[i-j] + Math.abs(h[i] - h[i-j]));
    		}
    	}

    	return dp[n-1];
    }

    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);

    	int n = sc.nextInt();
    	int k = sc.nextInt();
    	int[] h = new int[n];
    	for(int i = 0; i < n; i++) {
    		h[i] = sc.nextInt();
    	}

    	System.out.println(frog(h, n, k));
    }
}