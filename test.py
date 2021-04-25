import sys, random
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import re
# from bs4 import BeautifulSoup
# import math

def main():
    n, q = 300000, 300000
    print(n, q)
    arr = []
    for i in range(n):
        arr.append(random.randint(1, n))
    print(*arr)
    for i in range(q):
        a = random.randint(1, n)
        print(a, random.randint(a, n))


if __name__ == "__main__":
    main()