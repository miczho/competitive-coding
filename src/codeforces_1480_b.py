import sys, math

input = sys.stdin.readline

def theGreatHero(A, B, n, a, b):
	monsters = [[a[i], b[i]] for i in range(n)]
	monsters.sort(key=lambda x: x[0])

	i = 0
	while i < n and B > 0:
		turns = min(math.ceil(monsters[i][1] / A), math.ceil(B / monsters[i][0]))
		B -= monsters[i][0] * turns
		monsters[i][1] -= A * turns
		if monsters[i][1] <= 0:
			i += 1

	if i >= n: return 'YES'
	return 'NO'



def main():
	for t in range(int(input().strip())):
		A, B, n = map(int, input().strip().split())
		a, b = [int(i) for i in input().strip().split()], [int(i) for i in input().strip().split()]
		print(theGreatHero(A, B, n, a, b))


if __name__ == '__main__':
	main()