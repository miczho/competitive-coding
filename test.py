# import sys
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import re
# from bs4 import BeautifulSoup
# import math

def f(saving, arr1, arr2):
    n, dp = len(arr1), {}

    def dfs(i, j):
        if j == n: return 0

        if (i, j) not in dp:
            tmp = 0
            if i >= arr1[j]: tmp = max(tmp, dfs(i-arr1[j], j+1) + (arr2[j] - arr1[j]))
            tmp = max(tmp, dfs(i, j+1))
            dp[(i, j)] = tmp

        return dp[(i, j)]

    return dfs(saving, 0)


def g(n, rounds):
    total = [0 for _ in range(n+2)]

    for r in rounds:
        total[r[0]] += r[2]
        total[min(r[1]+1, n+1)] -= r[2]

    res = total[1]
    for i in range(2, n+1):
        total[i] += total[i-1]
        res = max(res, total[i])

    return res


def main():
    saving = 30000
    arr1 = [175, 133, 109, 210, 97]
    arr2 = [200, 125, 128, 228, 133]
    print(f(saving, arr1, arr2))


if __name__ == "__main__":
    main()