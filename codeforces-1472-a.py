import sys

def cardsForFriends():
	for _ in range(int(input())):
		w, h, n = map(int, input().split())
		ans, tmp = 1, 1
		while not w & 1:
			w //= 2
			ans += tmp
			tmp *= 2
		while not h & 1:
			h //= 2
			ans += tmp
			tmp *= 2
		if ans >= n:
			print('YES')
		else: print('NO')

def main():
    cardsForFriends()

if __name__ == "__main__":
    main()