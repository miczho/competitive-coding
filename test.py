import sys

class Solution:
	def __init__(self):
		self.d = {}
		self.xdiff = 0
		self.ydiff = 0

	def insert(self, x, y):
		self.d[x - self.xdiff] = y - self.ydiff

	def get(self, x):
		return self.d[x - self.xdiff] + self.ydiff

	def addToKey(self, x):
		self.xdiff += x

	def addToValue(self, y):
		self.ydiff += y


class Solution2:
	def __init__(self):
		self.d = {}

	def insert(self, x, y):
		self.d[x] = y

	def get(self, x):
		return self.d[x]

	def addToKey(self, x):
		# self.xdiff += x
		pass

	def addToValue(self, y):
		# self.ydiff += y
		pass


def test(q, q_args):
	n, s, ans = len(q), Solution(), 0

	for i in range(n):
		if q[i] == 'insert':
			s.insert(q_args[i][0], q_args[i][1])
		elif q[i] == 'get':
			ans += s.get(q_args[i][0])
		elif q[i] == 'addToKey':
			s.addToKey(q_args[i][0])
		else:
			s.addToValue(q_args[i][0])

	print(ans)


def main():
	test(['insert', 'insert', 'addToValue', 'addToKey', 'get'], [[1,2], [2,3], [2], [1], [3]])
	test(['insert', 'addToValue', 'get', 'insert', 'addToKey', 'addToValue', 'get'], [[1,2], [2], [1], [2,3], [1], [-1], [3]])

if __name__ == "__main__":
	main()