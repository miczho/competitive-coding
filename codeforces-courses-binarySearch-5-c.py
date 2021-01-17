import sys

input = sys.stdin.readline

class Soln:
	def __init__(self, n, k, a, b):
		self.n = n
		self.k = k
		self.a = a
		self.b = b

	def f(self, m):
		res = 0
		for i in self.a:
			if i >= m:
				break
			l = -1
			r = self.n
			while r > l + 1:
				m2 = (r + l) // 2
				if self.b[m2] < m - i:
					l = m2
				else:
					r = m2
			res += l + 1
		return res <= self.k-1

	def kthSum(self):
		l = 0
		r = 2 * 10**9 + 1
		while r > l + 1:
			m = (l + r) // 2
			if self.f(m):
				l = m
			else:
				r = m
		 
		# print(f(5))
		return l


def main():
	n, k = map(int, input().strip().split())
	a = list(map(int, input().strip().split()))
	b = list(map(int, input().strip().split()))
	a.sort(); b.sort()
	s = Soln(n, k, a, b)
	print(s.kthSum())


if __name__ == '__main__':
	main()