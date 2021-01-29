import sys, math

input = sys.stdin.readline

def inflation(n, k, p):
	ans, psum = 0, [0]

	for i in p:
		psum.append(psum[-1] + i)

	for i in range(1, n):
		targ = math.ceil(p[i] * 100 / k)
		# print(targ)
		# print(psum[i])
		ans = max(ans, targ - psum[i])

	return int(ans)


def main():
	for t in range(int(input().strip())):
		n, k = map(int, input().strip().split())
		p = [int(i) for i in input().strip().split()]
		print(inflation(n, k, p))


if __name__ == '__main__':
	main()