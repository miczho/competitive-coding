"""
#incomplete
"""

import sys
from collections import defaultdict

input = sys.stdin.readline

def LShape(r, c, arr):
	ones = [[dict()]*c for _ in range(r)]
	turns = [('left', 'up'), 
			('left', 'down'), 
			('right', 'up'), 
			('right', 'down'), 
			('up', 'left'), 
			('up', 'right'), 
			('down', 'left'), 
			('down', 'right')]
	res = 0
	
	for i in range(r):
		for j in range(c):
			if j == 0: ones[i][j]['left'] = arr[i][j]
			elif arr[i][j] == 1: ones[i][j]['left'] = arr[i][j] + ones[i][j-1].get(ones[i][j-1]['left'], 0)
		for j in range(c-1, -1, -1):
			if j == c-1: ones[i][j]['right'] = arr[i][j]
			elif arr[i][j] == 1: ones[i][j]['right'] = arr[i][j] + ones[i][j+1].get(ones[i][j+1]['right'], 0)
	for j in range(c):
		for i in range(r):
			if i == 0: ones[i][j]['up'] = arr[i][j]
			elif arr[i][j] == 1: ones[i][j]['up'] = arr[i][j] + ones[i-1][j].get(ones[i-1][j]['up'], 0)
		for i in range(r-1, -1, -1):
			if i == r-1: ones[i][j]['down'] = arr[i][j]
			elif arr[i][j] == 1: ones[i][j]['down'] = arr[i][j] + ones[i+1][j].get(ones[i+1][j]['down'], 0)
	print(ones)

	for i in range(r):
		for j in range(c):
			for turn in turns:
				if ones[i][j][turn[0]] >= 4 and ones[i][j][turn[1]] >= 2:
					# print(i, j, ones[i][j][turn[0]], ones[i][j][turn[1]])
					res += min(ones[i][j][turn[0]] // 2 - 1, ones[i][j][turn[1]] - 1)
	return res




def main():
	for t in range(int(input())):
		r, c = map(int, input().split())
		arr = []
		for _ in range(r):
			arr.append([int(i) for i in input().split()])
		print(f'Case #{t+1}: {LShape(r, c, arr)}')


if __name__ == '__main__':
	main()