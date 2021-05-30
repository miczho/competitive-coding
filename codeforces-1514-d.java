import java.io.*;
import java.util.*;
import java.lang.*;

class Main {
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


static class FastWriter {
        private static final int BUF_SIZE = 1<<13;
        private final byte[] buf = new byte[BUF_SIZE];
        private final OutputStream out;
        private int ptr = 0;
 
        private FastWriter(){out = null;}
 
        public FastWriter(OutputStream os)
        {
            this.out = os;
        }
 
        public FastWriter(String path)
        {
            try {
                this.out = new FileOutputStream(path);
            } catch (FileNotFoundException e) {
                throw new RuntimeException("FastWriter");
            }
        }
 
        public FastWriter write(byte b)
        {
            buf[ptr++] = b;
            if(ptr == BUF_SIZE)innerflush();
            return this;
        }
 
        public FastWriter write(char c)
        {
            return write((byte)c);
        }
 
        public FastWriter write(char[] s)
        {
            for(char c : s){
                buf[ptr++] = (byte)c;
                if(ptr == BUF_SIZE)innerflush();
            }
            return this;
        }
 
        public FastWriter write(String s)
        {
            s.chars().forEach(c -> {
                buf[ptr++] = (byte)c;
                if(ptr == BUF_SIZE)innerflush();
            });
            return this;
        }
 
        private static int countDigits(int l) {
            if (l >= 1000000000) return 10;
            if (l >= 100000000) return 9;
            if (l >= 10000000) return 8;
            if (l >= 1000000) return 7;
            if (l >= 100000) return 6;
            if (l >= 10000) return 5;
            if (l >= 1000) return 4;
            if (l >= 100) return 3;
            if (l >= 10) return 2;
            return 1;
        }
 
        public FastWriter write(int x)
        {
            if(x == Integer.MIN_VALUE){
                return write((long)x);
            }
            if(ptr + 12 >= BUF_SIZE)innerflush();
            if(x < 0){
                write((byte)'-');
                x = -x;
            }
            int d = countDigits(x);
            for(int i = ptr + d - 1;i >= ptr;i--){
                buf[i] = (byte)('0'+x%10);
                x /= 10;
            }
            ptr += d;
            return this;
        }
 
        private static int countDigits(long l) {
            if (l >= 1000000000000000000L) return 19;
            if (l >= 100000000000000000L) return 18;
            if (l >= 10000000000000000L) return 17;
            if (l >= 1000000000000000L) return 16;
            if (l >= 100000000000000L) return 15;
            if (l >= 10000000000000L) return 14;
            if (l >= 1000000000000L) return 13;
            if (l >= 100000000000L) return 12;
            if (l >= 10000000000L) return 11;
            if (l >= 1000000000L) return 10;
            if (l >= 100000000L) return 9;
            if (l >= 10000000L) return 8;
            if (l >= 1000000L) return 7;
            if (l >= 100000L) return 6;
            if (l >= 10000L) return 5;
            if (l >= 1000L) return 4;
            if (l >= 100L) return 3;
            if (l >= 10L) return 2;
            return 1;
        }
 
        public FastWriter write(long x)
        {
            if(x == Long.MIN_VALUE){
                return write("" + x);
            }
            if(ptr + 21 >= BUF_SIZE)innerflush();
            if(x < 0){
                write((byte)'-');
                x = -x;
            }
            int d = countDigits(x);
            for(int i = ptr + d - 1;i >= ptr;i--){
                buf[i] = (byte)('0'+x%10);
                x /= 10;
            }
            ptr += d;
            return this;
        }
 
        public FastWriter write(double x, int precision)
        {
            if(x < 0){
                write('-');
                x = -x;
            }
            x += Math.pow(10, -precision)/2;
            //      if(x < 0){ x = 0; }
            write((long)x).write(".");
            x -= (long)x;
            for(int i = 0;i < precision;i++){
                x *= 10;
                write((char)('0'+(int)x));
                x -= (int)x;
            }
            return this;
        }
 
        public FastWriter writeln(char c){
            return write(c).writeln();
        }
 
        public FastWriter writeln(int x){
            return write(x).writeln();
        }
 
        public FastWriter writeln(long x){
            return write(x).writeln();
        }
 
        public FastWriter writeln(double x, int precision){
            return write(x, precision).writeln();
        }
 
        public FastWriter write(int... xs)
        {
            boolean first = true;
            for(int x : xs) {
                if (!first) write(' ');
                first = false;
                write(x);
            }
            return this;
        }
 
        public FastWriter write(long... xs)
        {
            boolean first = true;
            for(long x : xs) {
                if (!first) write(' ');
                first = false;
                write(x);
            }
            return this;
        }
 
        public FastWriter writeln()
        {
            return write((byte)'\n');
        }
 
        public FastWriter writeln(int... xs)
        {
            return write(xs).writeln();
        }
 
        public FastWriter writeln(long... xs)
        {
            return write(xs).writeln();
        }
 
        public FastWriter writeln(char[] line)
        {
            return write(line).writeln();
        }
 
        public FastWriter writeln(char[]... map)
        {
            for(char[] line : map)write(line).writeln();
            return this;
        }
 
        public FastWriter writeln(String s)
        {
            return write(s).writeln();
        }
 
        private void innerflush()
        {
            try {
                out.write(buf, 0, ptr);
                ptr = 0;
            } catch (IOException e) {
                throw new RuntimeException("innerflush");
            }
        }
 
        public void flush()
        {
            innerflush();
            try {
                out.flush();
            } catch (IOException e) {
                throw new RuntimeException("flush");
            }
        }
 
        public FastWriter print(byte b) { return write(b); }
        public FastWriter print(char c) { return write(c); }
        public FastWriter print(char[] s) { return write(s); }
        public FastWriter print(String s) { return write(s); }
        public FastWriter print(int x) { return write(x); }
        public FastWriter print(long x) { return write(x); }
        public FastWriter print(double x, int precision) { return write(x, precision); }
        public FastWriter println(char c){ return writeln(c); }
        public FastWriter println(int x){ return writeln(x); }
        public FastWriter println(long x){ return writeln(x); }
        public FastWriter println(double x, int precision){ return writeln(x, precision); }
        public FastWriter print(int... xs) { return write(xs); }
        public FastWriter print(long... xs) { return write(xs); }
        public FastWriter println(int... xs) { return writeln(xs); }
        public FastWriter println(long... xs) { return writeln(xs); }
        public FastWriter println(char[] line) { return writeln(line); }
        public FastWriter println(char[]... map) { return writeln(map); }
        public FastWriter println(String s) { return writeln(s); }
        public FastWriter println() { return writeln(); }
    }
    
    // vars
    static final int MAXN = 300_300;
    static int n;
    static int q;
    static int[] arr = new int[MAXN];
    static List<Integer>[] sets;
    static int[] rand = new int[25];

    public static int bin(int pick, int val) {
        List<Integer> num_freq = sets[pick];
        // System.out.println(pick);

        int lo = -1; 
        int hi = num_freq.size();
        while(hi > lo + 1) {
            int mid = (lo + hi) / 2;
            if(num_freq.get(mid) <= val) {
                lo = mid;
            } else {
                hi = mid;
            }
        }

        return lo;
    }

    public static int cutAndStick(int l, int r) {
        int max_freq = (r - l + 2) / 2;
        int[] picks = new int[25];

        for(int i=0; i<25; i++) {
            int tmp = rand[i] % (r - l + 1) + l;
            picks[i] = arr[tmp];
        }
 
        for(int i=0; i<25; i++) {
            int lower = bin(picks[i], l-1);
            int upper = bin(picks[i], r);
            if(upper - lower > max_freq) {
                return 2 * (upper - lower) - r + l - 1;
            }
        }
 
        return 1;
    }

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        FastWriter out = new FastWriter(System.out);

        n = sc.nextInt();
        q = sc.nextInt();
        sets = new Vector[n+1];
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            sets[i+1] = new Vector<>();
        }

        for(int i = 0; i < n; i++) sets[arr[i]].add(i);

        for(int i = 0; i < 25; i++) rand[i] = (int)(Math.random() * 3 * 1000000);

        while(q-- > 0) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            l--; r--;

            out.println(cutAndStick(l, r));
        }
        out.flush();
    }
}