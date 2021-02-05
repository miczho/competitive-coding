import sys

input = sys.stdin.readline

def fencePainting(n, m, a, b, c):
	paint, colors, ans = {}, {}, [-1]*m

	for i in range(n):
		if a[i] != b[i]:
			if not paint.get(b[i]):
				paint[b[i]] = [i]
			else: paint[b[i]].append(i)
		if not colors.get(b[i]):
			colors[b[i]] = [i]
		else: colors[b[i]].append(i)
	# print(colors)

	i = m-1
	while i >= 0:
		if not paint.get(c[i]):
			if not colors.get(c[i]):
				if i == m-1 or ans[i+1] == -1:
					return -1
				ans[i] = ans[i+1]
			else:
				ans[i] = colors[c[i]][-1] + 1
		else:
			ans[i] = paint[c[i]].pop() + 1
			if len(paint[c[i]]) == 0:
				del paint[c[i]]
		i -= 1

	if paint:
		return -1
	return ans


def main():
	for t in range(int(input().strip())):
		n, m = map(int, input().strip().split())
		a, b, c = [int(i) for i in input().strip().split()], [int(i) for i in input().strip().split()], [int(i) for i in input().strip().split()]
		ans = fencePainting(n, m, a, b, c)
		if ans == -1:
			print('NO')
		else:
			print('YES')
			print(*ans)


if __name__ == '__main__':
	main()