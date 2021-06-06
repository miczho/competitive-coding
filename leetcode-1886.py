class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        n = len(mat)
        
        def equals(mat, target):
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        return False
            return True

        def rotate(mat):
            tmp = [[-1]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    tmp[i][j] = mat[j][n-i-1]

            return tmp

        for i in range(4):
            mat = rotate(mat)
            if equals(mat, target):
                return True

        return False


def main():
    s = Solution()
    print(s.findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))
    print(s.findRotation([[0,0],[0,1]], [[0,0],[1,0]]))     # true


main()