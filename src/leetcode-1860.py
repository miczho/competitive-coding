import sys

class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        i = 1
        while memory1 >= i or memory2 >= i:
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1

        return [i, memory1, memory2]


def main():
    pass


if __name__ == '__main__':
    main()