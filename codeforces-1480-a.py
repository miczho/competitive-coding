import sys

input = sys.stdin.readline

def yetAnotherStrGame(s):
	ans, switch = [' ']*len(s), 0
	for i in range(len(s)):
		if not switch:
			if s[i] != 'a':
				ans[i] = 'a'
			else:
				ans[i] = 'b'
		else:
			if s[i] != 'z':
				ans[i] = 'z'
			else:
				ans[i] = 'y'
		switch ^= 1

	return ''.join(ans)


def main():
	for t in range(int(input().strip())):
		s = input().strip()
		print(yetAnotherStrGame(s))


if __name__ == '__main__':
	main()