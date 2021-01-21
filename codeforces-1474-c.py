import sys
from collections import Counter

input = sys.stdin.readline

def arrayDestruct(n, arr):
	arr.sort()
	ans, x = [], 0

	for i in range(2*n-1):
		ans.clear()
		a, freq = arr.copy(), Counter(arr)
		y = a.pop()
		x = y + a[i]
		freq[y] -= 1
		freq[a[i]] -= 1
		ans.append([y, a[i]])
		while True:
			while a and freq[a[-1]] == 0:
				a.pop()
			if not a:
				break
			z = a[-1]
			freq[z] -= 1
			if freq[y-z] == 0:
				break
			else:
				freq[y-z] -= 1
				ans.append([z, y-z])
				y = z
		if len(ans) == n:
			break

	if len(ans) == n:
		print('YES')
		print(x)
		for i in ans:
			print(str(i[0]) + " " + str(i[1]))
	else:
		print('NO')




def main():
	for t in range(int(input().strip())):
		n, a = int(input().strip()), [int(i) for i in input().strip().split()]
		arrayDestruct(n, a)


if __name__ == '__main__':
	main()