# import sys
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import re
# from bs4 import BeautifulSoup
# import math

def main():
    s, stack, num = input(), [], []


    for ch in s:
        if ch == '(':
            stack.append('(')
        elif stack[-1] == '(':
            stack.append('')
            if ch >= 'a' and ch <= 'z':
                stack[-1] += ch
        elif ch >= 'a' and ch <= 'z':
            stack[-1] += ch
        elif ch >= '0' and ch <= '9':
            num.append(ch)
        elif ch == '}':
            s1 = stack.pop()
            s1 = s1 * int(''.join(num))
            if stack[-1] == '(':
                stack.pop()
            if stack and stack[-1] != '(':
                stack[-1] += s1
            else:
                stack.append(s1)
            num.clear()

    print(stack.pop())

# ((((ab){2}){3}){5}){2}c
# (((){2}){3}){4}

if __name__ == "__main__":
    main()