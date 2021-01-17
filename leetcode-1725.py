import sys

class Solution:
	def countGoodRectangles(self, r) -> int:
		ans, top = 0, 0
		for i in r:
			tmp = min(i[0], i[1])
			if tmp > top:
				top = tmp
				ans = 1
			elif tmp == top:
				ans += 1
		return ans

def main():
    s = Solution()
    print(s.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))


if __name__ == "__main__":
    main()