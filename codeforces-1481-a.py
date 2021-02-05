import sys, collections

input = sys.stdin.readline

def spaceNavigation(x, y, s):
	cnt = collections.Counter(s)
	if (cnt['R'] >= x and x >= 0) or (cnt['L'] >= -x and x < 0):
		if (cnt['U'] >= y and y >= 0) or (cnt['D'] >= -y and y < 0):
			return 'YES'
		return 'NO'
	return 'NO'


def main():
	for t in range(int(input().strip())):
		x, y = map(int, input().strip().split())
		s = input().strip()
		print(spaceNavigation(x, y, s))


if __name__ == '__main__':
	main()