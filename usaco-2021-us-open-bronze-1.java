import java.util.*;
import java.lang.*;

class Main {
    private int n;
    private int l;
    private int[] arr;

    public Main(int n, int l, int[] arr) {
        this.n = n;
        this.l = l;
        this.arr = arr;
    }

    public boolean find(int x) {
        int gt = 0; int lt = 0;
        for(int i : arr) {
            if(i >= x)
                gt++;
            else if(i == x - 1) 
                lt++;
        }
        int ans = gt + Math.min(lt, l);
        return ans >= x ? true : false;
    }

    public int acowdemiaI() {
        int l = 0; int r = 1_000_000;
        while(r > l + 1) {
            int m = (l + r) / 2;
            if(this.find(m))
                l = m;
            else
                r = m;
        }
        return l;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int l = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++)
            arr[i] = sc.nextInt();

        Main s = new Main(n, l, arr);
        System.out.println(s.acowdemiaI());
    }
}
