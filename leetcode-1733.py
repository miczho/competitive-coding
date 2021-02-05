import sys

# input = sys.stdin.readline

class Solution:
	def minimumTeachings(self, n, lang, fren) -> int:
		ans, m = float('inf'), len(lang)
		l = [set(i) for i in lang]

		for i in range(1,n+1):
			tmp, vis = 0, set()
			for x, y in fren:
				a = l[x-1]
				b = l[y-1]

				if not a & b:
					if i not in a and x not in vis:
						vis.add(x)
						tmp += 1
					if i not in b and y not in vis:
						vis.add(y)
						tmp += 1
				if tmp >= ans:
					break
			ans = min(ans, tmp)

		return ans


def main():
	s = Solution()
	print(s.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]))


if __name__ == '__main__':
	main()