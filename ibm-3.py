'''
https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
n x n
'''

import sys, random, time

def largestArea(samples):
    n = len(samples)
    maxSquare = [[0]*n for _ in range(n)]
    for i in range(n): 
        maxSquare[0][i] = samples[0][i]
        maxSquare[i][0] = samples[i][0]
    
    for i in range(1, n):
        for j in range(1, n):
            if samples[i][j]:
                maxSquare[i][j] = min(maxSquare[i-1][j-1], maxSquare[i][j-1], maxSquare[i-1][j]) + 1
            else: maxSquare[i][j] = 0
    
    return max(max(i) for i in maxSquare)
    

def main():
    print(largestArea([[1,1,1,1,1], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,1,1]]))

if __name__ == "__main__":
    main()