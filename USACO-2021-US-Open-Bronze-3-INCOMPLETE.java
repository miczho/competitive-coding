import java.util.*;

class Main {
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

    public boolean existsCow(int x, int y) {
        if(x >= 0 && y >= 0 && x < n && y < m && arr[x].charAt(y) == 'C')
            return true;
        return false;
    }

    public int acowdemiaIII() {
        Set<List> friends = new HashSet<>();
        Set<Integer[]> cow_list = new HashSet<>();
        int ans = 0;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) if(arr[i].charAt(j) == 'G') {
                List<Integer[]> cows = new ArrayList<>();
                for(int k = 0; k < 4; k++) {
                    int ii = i + imove[k];
                    int jj = j + jmove[k];
                    if(this.existsCow(ii, jj)) {
                        if(co)
                        Integer[] tmp = {ii, jj};
                        cows.add(tmp);
                    }
                    if(cows.size() > 2)
                        ans++;
                    else if(cows.size() == 2) {
                        Collections.sort(cows, new Comparator<Integer[]>() {
                            public int compare(Integer[] first, Integer[] second) {
                                if(first[0] != second[0])
                                    return first[0].compareTo(second[0]);
                                return first[1].compareTo(second[1]);
                            }
                        });
                        if(!friends.contains(cows)) {
                            friends.add(cows);
                            System.out.println(cows.get(0)[0]);
                        }
                    }
                }
            }
        }

        System.out.println(friends.toString());
        return friends.size() + ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int m = sc.nextInt();
        String[] arr = new String[n];
        for(int i = 0; i < n; i++)
            arr[i] = sc.next();


        Integer[] a = {1, 2}; Integer[] b = {4, 3};
        Integer[] c = {1, 2}; Integer[] d = {4, 3};
        Set<List> friends = new HashSet<>();
        List<Integer[]> p = new ArrayList<>();
        p.add(a); p.add(b);
        List<Integer[]> q = new ArrayList<>();
        q.add(c); q.add(d);
        friends.add(p);
        System.out.println(friends.contains(q));
        System.out.println(friends.toString());
        System.out.println(q.toString());

        // Main s = new Main(n, m, arr);
        // System.out.println(s.acowdemiaIII());
    }
}