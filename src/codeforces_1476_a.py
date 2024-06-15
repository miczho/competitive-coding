import sys, math

input = sys.stdin.readline

def kthDivisibleSum(n, k):
	if n > k:
		tmp = math.ceil(n / k)
		k *= tmp
	# print(k)

	if k % n:
		return k // n + 1
	else:
		return k // n


def main():
	for t in range(int(input().strip())):
		n, k = map(int, input().strip().split())
		print(kthDivisibleSum(n, k))


if __name__ == '__main__':
	main()