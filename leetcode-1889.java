import java.util.*;
import java.lang.*;

class Solution {
    static final int MOD = 1_000_000_007;
    static int n;
    static int[] packages;
    static int[][] boxes;

    public int minWastedSpace(int[] pac, int[][] bo) {
        n = pac.length; packages = pac; boxes = bo;
        long ans = Long.MAX_VALUE;

        Arrays.sort(packages);
        for(int[] bx : boxes) {
            Arrays.sort(bx);
            if(packages[packages.length-1] > bx[bx.length-1]) 
                continue;

            long tmp = 0;
            long prev = -1;
            for(int b : bx) {
                long curr = bsearch(b);
                tmp += ((curr - prev) * b);
                prev = curr;
            }
            ans = Math.min(ans, tmp);
        }

        long sum = 0;
        for(int x : packages)
            sum += x;

        return (ans == Long.MAX_VALUE) ? -1 : (int)((ans - sum) % MOD);
    }

    public int bsearch(int val) {
        int lo = -1; int hi = n;

        while(hi > lo + 1) {
            int mid = (lo + hi) / 2;
            if(packages[mid] <= val)
                lo = mid;
            else
                hi = mid;
        }

        return lo;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.minWastedSpace(new int[]{3,5,8,10,11,12}, new int[][]{{12},{11,9},{10,5,14}}));
    }
}