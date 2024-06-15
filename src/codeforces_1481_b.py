import sys

input = sys.stdin.readline

def newColony(n, k, h):
	cnt = 0

	h2 = h.copy()
	for i in range(n-1, 0, -1):
		if h2[i] > h2[i-1]: 
			cnt += h2[i] - h2[i-1]
			h2[i-1] = h2[i]
	# print(h2)

	if cnt < k:
		return -1
	else:
		p = 0
		while k > 0:
			while p > 0 and h[p-1] < h[p]:
				p -= 1
			while p < n-1 and h[p+1] <= h[p]:
				p += 1
			# print('p ' + str(p))
			h[p] += 1
			k -= 1
		return p+1


def main():
	for t in range(int(input().strip())):
		n, k = map(int, input().strip().split())
		h = [int(i) for i in input().strip().split()]
		print(newColony(n, k, h))


if __name__ == '__main__':
	main()