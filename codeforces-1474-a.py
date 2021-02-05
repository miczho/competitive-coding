import sys

def puzzleFuture(n, b):
	a = ['0']*n
	a[0] = '1'
	for i in range(1, n):
		if b[i-1] == b[i]:
			a[i] = str(int(a[i-1]) ^ 1)
		else: 
			if b[i-1] == '1': a[i] = a[i-1]
			else: a[i] = '1'
	return ''.join(a)


def main():
	for t in range(int(input())):
		n, b = int(input()), input()
		print(puzzleFuture(n, b))


if __name__ == '__main__':
	main()