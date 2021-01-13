import sys

def strangeBdayParty():
	for _ in range(int(input())):
		n, m = map(int, input().split())
		k = [int(i) for i in input().split()]
		c = [int(i) for i in input().split()]
		ans, base = 0, 0

		k.sort(reverse=True)
		for i in k:
			if i-1 > base: 
				ans += c[base]
				base += 1
			else: ans += c[i-1]

		print(ans)


def main():
    strangeBdayParty()

if __name__ == "__main__":
    main()