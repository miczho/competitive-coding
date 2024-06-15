import sys

input = sys.stdin.readline

class Soln:
	def __init__(self, n, k, arr):
		self.n = n
		self.k = k
		self.arr = arr


	def getRatio(self, m):
		x = []
		for i in self.arr:
			x.append(i[0] - m * i[1])
		x.sort(reverse=True)
		return sum(x[:self.k]) >= 0


	def pairSelection(self):
		l = -1
		r = 10**9
		for _ in range(100):
			m = (l + r) / 2
			if self.getRatio(m):
				l = m
			else:
				r = m
		return l


def main():
	n, k = map(int, input().strip().split())
	arr = []
	for i in range(n):
		arr.append(list(map(int, input().strip().split())))
	s = Soln(n, k, arr)
	print(s.pairSelection())


if __name__ == '__main__':
	main()