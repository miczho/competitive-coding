/*
#dp #knapsack
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.lang.*;

class Main {
    static int n;
    static int[] arr;

    public static void partitionsAgain() {
        int res = 0;
        int total = 0;
        for(int i = 0; i < n; i++) {
            if((arr[res] & -arr[res]) > (arr[i] & -arr[i])) res = i; // clearing all but the least significant bit
            total += arr[i];
        }

        if(total % 2 == 1) {
            System.out.println(0);
        } else {
            total /= 2;
            int[] dp = new int[total+1];
            
            // 0-1 knapsack
            for(int i = 0; i < n; i++) {
                for(int j = total; j >= arr[i]; j--) {
                    if(dp[j - arr[i]] == 1 || j == arr[i]) {
                        dp[j] = 1;
                    } 
                }
            }

            if(dp[total] == 1) {
                System.out.println(1);
                System.out.println(res+1);
            } else {
                System.out.println(0);
            }
        }
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        n = sc.nextInt();
        arr = new int[n];
        for(int i = 0; i < n; i++) 
            arr[i] = sc.nextInt();

        partitionsAgain();
    }

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
}