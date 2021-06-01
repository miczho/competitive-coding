import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    static class Reader {
        BufferedReader br;
        StringTokenizer st;

        public Reader(InputStream stream) {
            br = new BufferedReader(new InputStreamReader(stream));
        }
 
        public Reader(File file) {
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

    static class Writer {
        BufferedWriter bw;
        
        public Writer(OutputStream stream) {
            bw = new BufferedWriter(new OutputStreamWriter(stream));
        }

        public Writer(File file) {
            try {
                bw = new BufferedWriter(new FileWriter(file));
            } catch(IOException e) {
                e.printStackTrace();
            }
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
    
    static Reader in = new Reader(System.in);
    static Writer out = new Writer(System.out);

    // vars
    static int n;
    static int m;
    static char[] arr;

    public static void gameOfLife() {
        while(m-- > 0) {
            List<Integer> life = new ArrayList<>();
            for(int i = 0; i < n; i++) {
                if(arr[i] == '0') {
                    if((i-1) >= 0 && arr[i-1] == '1') {
                        if((i+1) >= n || arr[i+1] == '0') {
                            life.add(i);
                        }
                    } else {
                        if((i+1) < n && arr[i+1] == '1') {
                            life.add(i);
                        }
                    }
                }
            }

            if(life.isEmpty()) break;
            for(int i = 0; i < life.size(); i++) {
                arr[life.get(i)] = '1';
            }
        }

        out.println(new String(arr));
    }

    public static void main(String[] args) {
        int t = in.nextInt();
        while(t-- > 0) {
            n = in.nextInt();
            m = in.nextInt();
            arr = in.next().toCharArray();
            gameOfLife();
        }
        out.close();
    }
}