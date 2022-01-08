class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = set()
        for ch in s:
            if ch.isnumeric():
                num.add(ch)
        if len(num) < 2:
            return -1
        return sorted(list(num))[-2]