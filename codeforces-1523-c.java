import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader(InputStream stream) {
            br = new BufferedReader(new InputStreamReader(stream));
        }
 
        public FastReader(File file) {
            try {
                br = new BufferedReader(new FileReader(file));
            } catch(FileNotFoundException e) {
                e.printStackTrace();
            }
        }
 
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
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
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    static class FastWriter {
        BufferedWriter bw;
        
        public FastWriter(OutputStream stream) {
            bw = new BufferedWriter(new OutputStreamWriter(stream));
        }
        
        public void print(Object object) {
            try {
                bw.append("" + object);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        public void println(Object object) {
            print(object);
            try {
                bw.append("\n");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        public void close() {
            try {
                bw.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    
    // vars
    static int n;
    static FastReader in = new FastReader(System.in);
    static FastWriter out = new FastWriter(System.out);

    public static void compressionExpansion() {
        Stack<String> s = new Stack<>(); 
        while(n-- > 0) {
            String a = in.next();
            if(!s.isEmpty() && (Integer.parseInt(a) - 1) == Integer.parseInt(s.peek())) {
                s.pop();
                s.push(a);
            } else if(a.equals("1")) {
                s.push(a);
            } else {
                while((Integer.parseInt(a) - 1) != Integer.parseInt(s.peek())) {
                    s.pop();
                }
                s.pop();
                s.push(a);
            }
            out.println(String.join(".", s));
        }
    }

    public static void main(String[] args) throws IOException {
        int t = in.nextInt();
        while(t-- > 0) {
            n = in.nextInt();
            compressionExpansion();
        }
        out.close();
    }
}