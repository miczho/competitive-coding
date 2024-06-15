/*
#mods #modularInverse

A number 'b' is called the modular inverse of 'a' if:
    (a * b) % MOD = 1

In this use case, it wouldn't be wise to calculate combinations by dividing factorials 
bc (1) the values are too large and (2) modding the denominator can lead to a divide-by-zero error.
INSTEAD OF DIVIDING, we MULTIPLY with the modular inverse to get our combinations value.

TL;DR, (x / a) % MOD = (x * b) % MOD

*NOTE* there's no need to worry about this if overflow is not a concern

https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/
*/

import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    // this method works iff MOD is prime
    static final int MOD = 1_000_000_007;
    
    static int n, fac[], ifac[], dp[];
    static List<List<Integer>> g;
    
    public int waysToBuildRooms(int[] prevRoom) {
        n = prevRoom.length;
        g = new ArrayList<>();
        for (int i = 0; i < n; i++)
            g.add(new ArrayList<>());
        
        for (int i = 1; i < n; i++)
            g.get(prevRoom[i]).add(i);
        
        // calculating factorials and modular inverse of factorials
        fac = new int[n];
        ifac = new int[n];
        fac[0] = 1; ifac[0] = 1;
        for (int i = 1; i < n; i++) {
            fac[i] = (int)((long)(i) * fac[i-1] % MOD);
            // Fermat's little theorem: b = a^(MOD-2)
            ifac[i] = pow(fac[i], MOD-2);
        }
        
        dp = new int[n];
        
        return dfs(0);
    }
    
    // custom power function made to prevent overflow
    public static int pow(int a, int b) {
        if (b == 1) return a;

        if (b%2 == 1)
            return (int)((long)(1) * a * pow(a, b-1) % MOD);
        int res = pow(a, b/2);
        return (int)((long)(1) * res * res % MOD);
    }
    
    public static int nCr(int N, int R) {
        if (N < R) return 0;
        // n! / (n! (n-r)!) = n! * (1/n!) * (1/(n-r)!)
        return (int)((long)(1) * fac[N] * ifac[R] % MOD * ifac[N-R] % MOD);
    }
    
    public static int dfs(int node) {
        int res = 1;
        for (int child : g.get(node)) {
            // calculating combinations
            res = (int)((long)(res) * dfs(child) % MOD * nCr(dp[node]+dp[child], dp[child]) % MOD);
            dp[node] += dp[child];
        }
        
        dp[node] += 1;
        return res;
    }
}