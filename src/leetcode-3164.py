from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pass

def prime_factors(n):
    result = []

    # check for 2
    while n % 2 == 0:
        result.append(2)
        n //= 2

    # check for odd values up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 2

    # if n > 1, then it's a prime
    if n > 1:
        result.append(n)

    return result
