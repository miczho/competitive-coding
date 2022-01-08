import sys

def longJumps():
	for _ in range(int(input())):
		n, a = int(input()), [int(i) for i in input().split()]
		b = [0]*(n+1)
		for i in range(n):
			if i + a[i] < n: b[i+a[i]] = max(b[i+a[i]], b[i] + a[i])
			else: b[n] = max(b[n],  b[i] + a[i])
		print(b[-1])

def main():
    longJumps()

if __name__ == "__main__":
    main()