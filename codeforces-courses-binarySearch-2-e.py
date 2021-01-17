'''
#binsearch #binsearch-float
'''

import sys

def equation(c):
	l = -1
	r = 10**5

	# l and r get squeezed REALLY close to each other
	for _ in range(100):
		m = (l + r) / 2
		if m**2 + m**0.5 <= c:
			l = m
		else:
			r = m
	return l


def main():
	print(equation(float(input())))


if __name__ == '__main__':
	main()