import sys

def noMoreInversions(n, k):
	invert = n - k
	

def main():
    for t in range(int(input())):
    	n, k = map(int, input().split())
    	print(noMoreInversions(n, k))

if __name__ == "__main__":
    main()