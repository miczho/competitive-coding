class Solution(object):
    def minFlips(self, ss):
        """
        :type s: str
        :rtype: int
        """
        n = len(ss)
        if n == 1: return 0

        s = list()
        a1, a2 = list(), list()
        turn = 1
        for _ in range(2):
            for x in ss:
                if x == '0':
                    s.append(0)
                else:
                    s.append(1)
                a1.append(turn)
                a2.append(turn^1)
                turn ^= 1

        ans = float('inf')
        cnt1, cnt2 = 0, 0
        for i in range(2*n):
            if s[i] != a1[i]: cnt1 += 1
            if s[i] != a2[i]: cnt2 += 1

            if i >= n:
                if s[i-n] != a1[i-n]: cnt1 -= 1
                if s[i-n] != a2[i-n]: cnt2 -= 1

            if i >= n-1:
                ans = min(ans, cnt1, cnt2)

        return ans


def main():
    s = Solution()
    print(s.minFlips("01001001101"))    # 2


main()