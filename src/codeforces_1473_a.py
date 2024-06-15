import sys

def replacingElements(n, d, a):
	a.sort()
	if a[-1] <= d or a[0] + a[1] <= d: return 'YES'
	return 'NO'

def main():
    for _ in range(int(input())):
    	n, d = map(int, input().split())
    	a = [int(i) for i in input().split()]
    	print(replacingElements(n, d, a))

if __name__ == "__main__":
    main()