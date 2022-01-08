import sys

class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(box), len(box[0])
        ans = [["."]*m for _ in range(n)]

        for j in range(n-1, -1, -1):
            for i in range(m):
                if box[i][j] == "*":
                    ans[j][m-i-1] = "*"
                elif box[i][j] == "#":
                    jj = j
                    while jj < n-1:
                        if box[i][jj+1] == ".":
                            jj += 1
                        else:
                            break
                    box[i][j] = "."
                    box[i][jj] = "#"
                    ans[jj][m-i-1] = "#"

        return ans


def main():
    pass


if __name__ == '__main__':
    main()