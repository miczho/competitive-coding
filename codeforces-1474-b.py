import sys

MAXN = 3*10_000 + 10
prime = {}
for i in range(2, MAXN):
	prime[i] = 1

def sieve():
	for i in range(2, MAXN):
		if i in prime:
			j = 2
			while i*j < MAXN:
				if i*j in prime: prime.pop(i*j)
				j += 1


def diffDivisors(d):
	a, b, x = 0, 0, 1
	for i in prime.keys():
		if i - x >= d:
			if not a: 
				a = i
				x = i
			elif not b: 
				b = i
				break
	return a*b


def main():
	sieve()
	for t in range(int(input())):
		d = int(input())
		print(diffDivisors(d))


if __name__ == '__main__':
	main()