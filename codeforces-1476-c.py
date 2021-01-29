import sys

input = sys.stdin.readline

def longestSimpleCycle(n, c, a, b):
	ans, tmp = 0, abs(a[1] - b[1])

	for i in range(1, n):
		if a[i] == b[i]:
			tmp = 0
		elif i != 1:
			tmp -= c[i-1] - 1
			tmp += min(a[i], b[i]) - 1 + c[i-1] - max(a[i], b[i])
			if abs(a[i] - b[i]) > tmp:
				tmp = abs(a[i] - b[i])
		tmp += c[i] + 1
		ans = max(ans, tmp)

	return ans


def main():
	for t in range(int(input().strip())):
		n, c, a, b = int(input().strip()), [int(i) for i in input().strip().split()], [int(i) for i in input().strip().split()], [int(i) for i in input().strip().split()]
		print(longestSimpleCycle(n, c, a, b))


if __name__ == '__main__':
	main()