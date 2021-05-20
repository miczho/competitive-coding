import java.util.*;
import java.lang.*;

class Main {
    int n;
    int k;
    int l;
    Integer[] arr;

    public Main(int n, int k, int l, Integer[] arr) {
        this.n = n;
        this.k = k;
        this.l = l;
        this.arr = arr;
    }

    public boolean find(int mid) {
        if(arr[mid-1] < (mid - k)) return false;

        long diff = 0;
        for(int i = 0; i < mid; i++) {
            diff += (long)(Math.max(0, mid - arr[i]));
        }

        return diff <= (long)(k) * (long)(l);
    }

    public int acowdemia() {
        int left = 0; int right = n+1;
        while(right > (left + 1)) {
            int mid = (left + right) / 2;
            if(this.find(mid))
                left = mid;
            else
                right = mid;
        }

        return left;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int k = sc.nextInt(); int l = sc.nextInt();
        Integer[] arr = new Integer[n];
        for(int i = 0; i < n; i++) arr[i] = sc.nextInt();

        Arrays.sort(arr, Comparator.reverseOrder());

        Main s = new Main(n, k, l, arr);
        System.out.println(s.acowdemia());
    }
}