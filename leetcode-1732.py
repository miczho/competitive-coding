import sys

# input = sys.stdin.readline

class Solution:
	def largestAltitude(self, gain) -> int:
		ans, cnt = 0, 0
		for i in gain:
			cnt += i
			ans = max(ans, cnt)

		return ans


def main():
	pass


if __name__ == '__main__':
	main()