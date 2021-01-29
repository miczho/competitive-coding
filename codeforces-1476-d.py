import sys

input = sys.stdin.readline

def journey(n, s):
	left, right = [[0]*(n+1) for _ in range(2)], [[0]*(n+1) for _ in range(2)]
	ans, m = [], ['L', 'R']

	for j in range(1, n+1):
		for i in range(2):
			if m[i] == s[j-1]:
				left[i][j] = 1 + left[i^1][j-1]

	for j in range(n-1, -1, -1):
		for i in range(2):
			if m[i] == s[j]:
				right[i][j] = 1 + right[i^1][j+1]

	for i in range(n+1):
		ans.append(str(1 + left[0][i] + right[1][i]))

	return ans


def main():
	for t in range(int(input().strip())):
		n, s = int(input().strip()), input().strip()
		print(*journey(n, s))


if __name__ == '__main__':
	main()