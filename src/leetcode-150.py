class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = {
              '+': lambda a, b: a+b, 
              '-': lambda a, b: a-b, 
              '*': lambda a, b: a*b, 
              '/': lambda a, b: int(float(a)/b), 
              '^': lambda a, b: a**b,
             }
        
        stack = list()
        
        for x in tokens:
            try:
                stack.append(int(x))
            except ValueError:
                b, a = stack.pop(), stack.pop()
                stack.append(op[x](a, b))
        
        return stack.pop()