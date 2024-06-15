import java.io.*;
import java.util.*;
import java.lang.*;

class Solution {
    public static char[] infixToPostfix(String exp) {
        Stack<Character> st = new Stack<>();
        String res = "";
        
        for(char x : exp.toCharArray()) {
            if(Character.isDigit(x)) {
                res += x;
            } else if(x == '(') {
                st.push(x);
            } else {
                while(!st.isEmpty() && st.peek() != '(')
                    res += st.pop();
                
                if(x == ')') st.pop();
                else st.push(x);
            }
        }
        
        while(!st.isEmpty())
            res += st.pop();
        
        return res.toCharArray();
    }
    
    public static int minOperationsToFlip(String expression) {
        char[] postfix = infixToPostfix(expression);
        
        Stack<Integer> reg = new Stack<>();
        Stack<Integer> one = new Stack<>();
        Stack<Integer> zero = new Stack<>();
        
        for(char x : postfix) {
            if(Character.isDigit(x)) {
                int i = x - '0';
                reg.push(i);
                one.push(i^1);
                zero.push(i^0);
            } else {
                int r2 = reg.pop(), o2 = one.pop(), z2 = zero.pop();
                int r1 = reg.pop(), o1 = one.pop(), z1 = zero.pop();
                
                if(x == '&') {
                    reg.push(r1 & r2);
                    
                    if(reg.peek() == 0) {
                        int j = o1+o2;
                        j = Math.min(j, 1 + Math.min(z1+o2, o1+z2));
                        
                        one.push(j);
                        zero.push(0);
                    } else {
                        int j = Math.min(z1+o2, o1+z2);
                        j = Math.min(j, 1+z1+z2);
                        
                        one.push(0);
                        zero.push(j);
                    }
                } else {
                    reg.push(r1 | r2);
                    
                    if(reg.peek() == 0) {
                        int j = Math.min(o1+z2, z1+o2);
                        j = Math.min(j, 1+o1+o2);
                        
                        one.push(j);
                        zero.push(0);
                    } else {
                        int j = z1+z2;
                        j = Math.min(j, 1 + Math.min(o1+z2, z1+o2));
                        
                        one.push(0);
                        zero.push(j);
                    }
                }
            }
        }
        
        return (reg.peek() == 0) ? one.peek() : zero.peek();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.minOperationsToFlip("(0&0)&(0&0&0)"));
    }
}