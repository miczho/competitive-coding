import sys

input = sys.stdin.readline
d = {}

def find(i):
	if d.get(i) == None:
		print('? {:d}'.format(i))
		sys.stdout.flush()
		d[i] = int(input().strip())
	return d.get(i)


def searchLocalMin(n):
	d[0], d[n+1] = float('inf'), float('inf')

	l, r = 0, n+1
	for i in range(100):
		m = (l + r) // 2
		if (find(m) < find(m+1)) and (find(m) < find(m-1)):
			return '! {:d}'.format(m)
		elif find(m) > find(m-1):
			r = m
		else:
			l = m


def main():
	n = int(input().strip())
	print(searchLocalMin(n))


if __name__ == '__main__':
	main()