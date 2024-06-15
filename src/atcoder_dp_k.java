/*
https://atcoder.jp/contests/dp/tasks/dp_k

Nim is a game where two ppl take turns removing objects from a pile
#gameTheory #nim
*/

import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for(int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        // default is false
        boolean[] dp = new boolean[k+1];

        for(int i = 0; i <= k; i++) {
            for(int j : a) {
                // any position with no moves is losing
                // a position is losing if ALL moves are to a winning position
                // a position is winning if THERE EXISTS a move to a losing position
                if(j <= i && !dp[i - j]) {
                    dp[i] = true;
                }
            }
        }
        // System.out.println(Arrays.toString(dp));

        if(dp[k])
            System.out.println("First");
        else
            System.out.println("Second");
    }
}