'''
player1 tries to MAXIMIZE score(player1) - score(player2)
player2 tries to MINIMIZE score(player1) - score(player2)
THIS IS THE BOTTOM UP SOLUTION
#dp #game-theory #minimax
'''

import sys

input = sys.stdin.readline

def dequeGame(n, arr):
	dp = [[0]*n for _ in range(n)]

	for i in range(n):
		dp[i][i] = arr[i]

	# for i from n-1 to 0, fill the values from i+1 to n-1
	'''
	0  7  8  9  10
	0  0  4  5  6
	0  0  0  2  3
	0  0  0  0  1
	0  0  0  0  0
	'''
	# alternatively you can fill diagonally
	for i in range(n-1, -1, -1):
		for j in range(i+1, n):
			dp[i][j] = max(arr[i] - dp[i+1][j], arr[j] - dp[i][j-1])
			# for row in dp:
			# 	print(*row)
			# print()

	return dp[0][-1]


def main():
	n, arr = int(input().strip()), [int(i) for i in input().strip().split()] 
	print(dequeGame(n, arr))


if __name__ == '__main__':
	main()