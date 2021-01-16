import sys

def noMoreInversions(n, k):
	p = [str(i) for i in range(1, k+1)]

	for i in range(2*k-n-1, (3*k-n-1)//2):
		p[i], p[3*k-n-2-i] = p[3*k-n-2-i], p[i]
	
	return ' '.join(p)
	

def main():
    for t in range(int(input())):
    	n, k = map(int, input().split())
    	print(noMoreInversions(n, k))


if __name__ == "__main__":
    main()