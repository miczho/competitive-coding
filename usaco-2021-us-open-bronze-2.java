import java.util.*;

class Main {
    private int k;
    private int n;
    private String[] ppl;
    private String[][] arr;

    public Main(int k, int n, String[] ppl, String[][] arr) {
        this.k = k;
        this.n = n;
        this.ppl = ppl;
        this.arr = arr;
    }

    public void acowdemiaII() {
        Map<String, Integer> freq = new HashMap<String, Integer>();

        for(int i=0; i<k; i++) {
            int cnt = 0;
            for(int j=1; j<n; j++) {
                if(arr[i][j-1].compareTo(arr[i][j]) > 0) {
                    cnt++;
                }
                freq.put(arr[i][j], freq.getOrDefault(arr[i][j], 0) + cnt);
            }
        }

        for(int i=0; i<n; i++) {
            String[] res = new String[n];
            int a = freq.getOrDefault(ppl[i], 0);
            for(int j=0; j<n; j++) {
                if(i == j) {
                    res[j] = "B";
                    continue;
                }
                int b = freq.getOrDefault(ppl[j], 0);
                if(a > b)
                    res[j] = "1";
                else if(a < b)
                    res[j] = "0";
                else
                    res[j] = "?";
            }
            System.out.println(String.join("", res));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt(); int n = sc.nextInt();
        String[] ppl = new String[n];
        for(int i=0; i<n; i++)
            ppl[i] = sc.next();
        String[][] arr = new String[k][n];
        for(int i=0; i<k; i++)
            for(int j=0; j<n; j++)
                arr[i][j] = sc.next();

        Main s = new Main(k, n, ppl, arr);
        s.acowdemiaII();
    }
}
