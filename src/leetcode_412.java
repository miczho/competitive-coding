class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ans = new ArrayList<String>();
        if(n == 0) return ans;

        for(int i = 1; i < n+1; i++) {
            boolean a = (i % 3 == 0);
            boolean b = (i % 5 == 0);
            if(a && b) ans.add("FizzBuzz");
            else if(a) ans.add("Fizz");
            else if(b) ans.add("Buzz");
            else ans.add(Integer.toString(i));
        }

        return ans;
    }
}
