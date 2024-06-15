"""
#calculator #postfix #reversePolish

https://leetcode.com/problems/basic-calculator/
"""

class Solution(object):
    @staticmethod
    def infixToPostfix(s):
        """
        converts a *valid* infix str to postfix list
        """
        operators = {'+', '-', '*', '/', '^'}

        def isUnary(pos):
            if s[pos] == '+' or s[pos] == '-':
                if pos == 0:
                    return True
                elif s[pos-1] in operators:
                    return True
                elif s[pos-1] == '(':
                    return True
            return False

        def precedence(ch):
            if ch == '+' or ch == '-':
                return 1
            elif ch == '*' or ch == '/':
                return 2
            elif ch == '^':
                return 3
            return -1

        res, stack, val = (list() for _ in range(3))
        
        # Removing white space is needed for unary check to work
        s = s.replace(' ', '')
        # Looping through the infix
        for i, ch in enumerate(s):
            if ch.isdigit():
                val.append(ch)
            else:
                # Appending operands (numbers)
                if isUnary(i):
                    res.append('0')
                elif val:
                    res.append(''.join(val))
                    val.clear()
                # Appending operators
                if ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    while stack[-1] != '(':
                        res.append(stack.pop())
                    stack.pop()
                elif ch in operators:
                    while stack and precedence(ch) <= precedence(stack[-1]):
                        res.append(stack.pop())
                    stack.append(ch)
        
        # Appending leftover operands and operators
        if val:
            res.append(''.join(val))
        while stack:
            res.append(stack.pop())

        return res
    

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        op = {
              '+': lambda a, b: a+b, 
              '-': lambda a, b: a-b, 
              '*': lambda a, b: a*b, 
              '/': lambda a, b: a/b, 
              '^': lambda a, b: a**b,
             }

        postfix = self.infixToPostfix(s)
        stack = list()
        # print(postfix)

        for x in postfix:
            try:
                stack.append(int(x))
            except ValueError:
                b, a = stack.pop(), stack.pop()
                stack.append(op[x](a, b))

        return stack.pop()


def main():
    sol = Solution()
    print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(sol.calculate("2-1+2"))
    print(sol.calculate("+48 + -48"))
    print(sol.calculate("- (3 + (4 + 5))"))
    print(sol.calculate("0"))


main()