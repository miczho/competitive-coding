'''
This style is easy to edit; l and r never cross each other.
#binsearch
'''

import sys

def closestToTheLeft(n, k, arr, target):
	# l and r are intentionally initialized out of bounds
	# careful bc -1 actually points to the last array element in python
	l = -1
	r = len(arr)

	while r > l + 1:
		m = l + (r - l) // 2
		if arr[m] <= target:
			l = m 
		else:
			r = m

	# adding 1 since the array is 1-indexed in the problem
	return l+1


def main():
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	tests = list(map(int, input().split()))

	for target in tests:
		print(closestToTheLeft(n, k, arr, target))


if __name__ == "__main__":
    main()