import java.io.*;
import java.util.*;

class Main {
    private int n;
    private int[] arr;
    private Map<Integer, List<Integer>> map;
    private Random rand;

    public Main(int n, int[] arr, Map<Integer, List<Integer>> map) {
        this.n = n;
        this.arr = arr;
        this.map = map;
        this.rand = new Random();
    }

    public int bin(int pick, int val) {
        List<Integer> num_freq = this.map.get(pick);

        int l = -1; int r = num_freq.size();
        while(r > l + 1) {
            int m = (l + r) / 2;
            if(num_freq.get(m) <= val) {
                l = m;
            } else {
                r = m;
            }
        }

        return l;
    }

    public int cutAndStick(int l, int r) {
        int max_freq = (r - l + 2) / 2;
        int[] picks = new int[25];
        
        for(int i=0; i<25; i++) {
            int tmp = this.rand.nextInt(r-l+1) + l;
            picks[i] = this.arr[tmp];
        }

        for(int i=0; i<25; i++) {
            int lower = this.bin(picks[i], l-1);
            int upper = this.bin(picks[i], r);
            if(upper - lower > max_freq) {
                return 2 * (upper - lower) - r + l - 1;
            }
        }

        return 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); int q = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        Map<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            map.putIfAbsent(arr[i], new ArrayList<Integer>());
            map.get(arr[i]).add(i);
        }

        Main sol = new Main(n, arr, map);
        StringBuilder ans = new StringBuilder();
        for(int z=0; z<q; z++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken()); int r = Integer.parseInt(st.nextToken());
            l--; r--;
            ans.append(sol.cutAndStick(l, r));
            ans.append("\n");
        }
        System.out.print(ans.toString());
    }
}