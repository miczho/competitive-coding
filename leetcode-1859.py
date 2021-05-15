import sys

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = [i for i in s.split()]

        ans = ["0"]*len(words)
        for w in words:
            ans[int(w[-1]) - 1] = w[:-1]

        return " ".join(ans)


def main():
    s = Solution()
    print(s.sortSentence("is2 sentence4 This1 a3"))


if __name__ == '__main__':
    main()