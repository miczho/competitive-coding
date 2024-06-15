import sys, math

def lcm(x, y):
	return abs(x * y) // math.gcd(x, y)

def stringLcm(s, t):
	m, n = len(s), len(t)
	LCM = lcm(m, n)
	if s * (LCM // m) == t * (LCM // n): return s * (LCM // m)
	return -1

def main():
    for q in range(int(input())):
    	s, t = input(), input()
    	print(stringLcm(s, t))

if __name__ == "__main__":
    main()