import java.util.*;

public class Main {
    static final int[] imove = {-1, 0, 0, 1};
    static final int[] jmove = {0, -1, 1, 0};

    private int n;
    private int m;
    private String[] arr;

    public Main(int n, int m, String[] arr) {
        this.n = n;
        this.m = m;
        this.arr = arr;
    }

    public boolean inBounds(int x, int y) {
        if(x >= 0 && y >= 0 && x < n && y < m)
            return true;
        return false;
    }

    public int acowdemiaIII() {
        Set<Map.Entry> friends = new HashSet<>();
        // Map.Entry<Integer, Integer> pair = new AbstractMap.SimpleImmutableEntry<>(0, 1);

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(arr[i].charAt(j) == 'G') {
                    List<Map.Entry> cows = new ArrayList<>();
                    for(int k = 0; k < 4; k++) {
                        int ii = i + imove[k];
                        int jj = j + jmove[k];
                        if(this.inBounds(ii, jj) && arr[ii].charAt(jj) == 'C')
                            cows.add(new AbstractMap.SimpleImmutableEntry<>(ii, jj));
                    }
                    for(int a = 0; a < cows.size(); a++) {
                        boolean tmp = true;
                        for(int b = a+1; b < cows.size(); b++) {
                            Map.Entry<Map.Entry, Map.Entry> pair = new AbstractMap.SimpleImmutableEntry<>(cows.get(a), cows.get(b));
                            if(!friends.contains(pair)) {
                                friends.add(pair);
                                friends.add(new AbstractMap.SimpleImmutableEntry<>(cows.get(b), cows.get(a)));
                                tmp = true;
                                break;
                            }
                        }
                        if(tmp)
                            break;
                    }
                }
            }
        }

        return friends.size() / 2;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int m = sc.nextInt();
        String[] arr = new String[n];
        for(int i = 0; i < n; i++)
            arr[i] = sc.next();

        Main s = new Main(n, m, arr);
        System.out.println(s.acowdemiaIII());
    }
}