import sys, collections

def fairDivision():
	for _ in range(int(input())):
		n, a = int(input()), list(map(int, input().split()))
		c = collections.Counter(a)
		if not sum(a) & 1: 
			if not c[2] & 1: print('YES')
			elif c[1] >= 2: print('YES')
			else: print('NO')
		else: print('NO')

def main():
    fairDivision()

if __name__ == "__main__":
    main()