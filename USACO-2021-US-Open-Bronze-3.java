import java.util.*;

class Main {
    private int n;
    private int m;
    private char[][] arr;

    public Main(int n, int m, char[][] arr) {
        this.n = n;
        this.m = m;
        this.arr = arr;
    }


    public int acowdemiaIII() {
        int ans = 0;

        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= m; j++) {
                if(arr[i][j] == 'G') {
                    if((arr[i-1][j] == 'C' && arr[i+1][j] == 'C') || (arr[i][j-1] == 'C' && arr[i][j+1] == 'C')){
                        ans++;
                        arr[i][j] = '.';
                    }
                }
            }
        }

        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= m; j++) {
                if(arr[i][j] == 'C') {
                    if(arr[i+1][j-1] == 'C') {
                        if(arr[i][j-1] == 'G') {
                            ans++;
                            arr[i][j-1] = '.';
                        } else if(arr[i+1][j] == 'G') {
                            ans++;
                            arr[i+1][j] = '.';
                        }
                    } 
                    if(arr[i+1][j+1] == 'C') {
                        if(arr[i][j+1] == 'G') {
                            ans++;
                            arr[i][j+1] = '.';
                        } else if(arr[i+1][j] == 'G') {
                            ans++;
                            arr[i+1][j] = '.';
                        }
                    }
                }
            }
        }

        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int m = sc.nextInt();
        char[][] arr = new char[n+2][];
        arr[0] = new char[m+2]; Arrays.fill(arr[0], '.');
        arr[n+1] = arr[0];
        for(int i = 1; i <= n; i++)
            arr[i] = ('.' + sc.next() + '.').toCharArray();

        Main s = new Main(n, m, arr);
        System.out.println(s.acowdemiaIII());
    }
}
