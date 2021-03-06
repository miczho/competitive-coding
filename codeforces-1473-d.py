'''
#python-io
'''

import sys

# need this
# normal input() is much slower
input = sys.stdin.readline 

MAXN = 2 * 100_000 + 5
cnt, top, bot = [0]*MAXN, [[0]*MAXN for i in range(2)], [[0]*MAXN for i in range(2)]

def program(n, m, s):
	for i in range(n):
		if s[i] == '+': cnt[i+1] = cnt[i] + 1
		else: cnt[i+1] = cnt[i] - 1
	for i in range(1, n+1):
		top[0][i] = bot[0][i] = top[1][i] = bot[1][i] = cnt[i]	
	for i in range(1, n+1):
		top[0][i] = max(top[0][i], top[0][i-1])
		bot[0][i] = min(bot[0][i], bot[0][i-1])	
	for i in range(n-1, -1, -1):
		top[1][i] = max(top[1][i], top[1][i+1])
		bot[1][i] = min(bot[1][i], bot[1][i+1])

	for _ in range(m):
		# strip() removes any whitespace (???)
		l, r = map(int, input().split())
		diff = cnt[l-1] - cnt[r]
		if r < n:
			t = max(top[0][l-1], top[1][r+1] + diff)
			b = min(bot[0][l-1], bot[1][r+1] + diff)
		else:
			t, b = top[0][l-1], bot[0][l-1]
		print(str(t-b+1) + '\n')
		

def main():
	for t in range(int(input())):
		n, m = map(int, input().split())
		s = input().strip()
		program(n, m, s)

if __name__ == "__main__":
    main()