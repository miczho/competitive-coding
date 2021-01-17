import sys

class Solution:
	def largestSubmatrix(self, matrix) -> int:
		m, n = len(matrix), len(matrix[0])
		ans, arr = 0, [[0]*n for i in range(m)]

		for i in range(n):
			if matrix[0][i]: arr[0][i] = 1
		for j in range(n):
			for i in range(1, m):
				if matrix[i][j]: arr[i][j] = arr[i-1][j] + 1
		
		for i in range(m):
			arr[i].sort(reverse=True)
			for j in range(n):
				ans = max(ans, arr[i][j] * (j+1))

		return ans


def main():
	s = Solution()
	print(s.largestSubmatrix([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1],
							[0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,1,1,1]]))


if __name__ == '__main__':
	main()