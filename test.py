import sys, random
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import re
# from bs4 import BeautifulSoup
# import math

def main():
    t = int(input())
    for j in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        
        value = {}
        fa, ca = 0, 0
        
        for i in range(n):
          if a[i] in value:
            ca += value[a[i]]
          else:
            value[a[i]]=0
          value[a[i]] += i+1
          fa += ca
          print(fa)
        
        print(value)
        print(fa)

if __name__ == "__main__":
    main()