import sys, math
from collections import defaultdict

class Solution:
	def tupleSameProduct(self, nums) -> int:
		n, d, ans = len(nums), defaultdict(int), 0
		for i in range(n):
			for j in range(i+1, n):
				d[nums[i] * nums[j]] += 1
		# print(d)

		for i in d.values():
			ans += i * (i-1) // 2
		return ans * 8


def main():
	s = Solution()
	print(s.tupleSameProduct([1,2,4,5,10]))


if __name__ == '__main__':
	main()