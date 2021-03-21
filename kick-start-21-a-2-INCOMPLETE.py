import sys

input = sys.stdin.readline

def LShape(r, c, arr):
	pass


def main():
	for t in range(int(input())):
		r, c = map(int, input().split())
		arr = []
		for _ in range(r):
			arr.append([int(i) for i in input().split()])
		print(f'Case #{t+1}: {LShape(r, c, arr)}')


if __name__ == '__main__':
	main()