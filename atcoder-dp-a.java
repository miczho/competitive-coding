import java.util.*;

class Main {
    public static int frog(int[] h, int n) {
    	int[] dp = new int[n];

    	for(int i = 1; i < n; i++) {
    		dp[i] = dp[i-1] + Math.abs(h[i] - h[i-1]);
    		if(i > 1)
    			dp[i] = Math.min(dp[i], dp[i-2] + Math.abs(h[i] - h[i-2]));
    	}

    	return dp[n-1];
    }

    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);

    	int n = sc.nextInt();
    	int[] h = new int[n];
    	for(int i = 0; i < n; i++) {
    		h[i] = sc.nextInt();
    	}

    	System.out.println(frog(h, n));
    }
}